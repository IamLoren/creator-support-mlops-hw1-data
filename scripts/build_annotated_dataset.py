import argparse
import json
from collections import Counter
from pathlib import Path


REQUIRED_DATA_FIELDS = {
    "id",
    "scenario_id",
    "text",
    "language",
    "domain",
    "source",
}

ALLOWED_LANGUAGES = {
    "uk",
    "en",
}

ALLOWED_DOMAINS = {
    "education",
    "fitness",
    "beauty",
    "professional_services",
}

ALLOWED_SOURCES = {
    "manual",
    "synthetic",
    "production_anonymized",
}

ALLOWED_INTENTS = {
    "ACCESS_ACCOUNT",
    "TECHNICAL_ISSUE",
    "SCHEDULE_DEADLINE",
    "SERVICE_INFO",
    "CONTENT_USAGE_QUESTION",
    "CHANGE_CANCEL",
    "FEEDBACK_COMPLAINT",
    "HUMAN_SUPPORT",
    "OTHER",
}


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Transform a Label Studio export into the canonical "
            "customer-support intent dataset."
        )
    )

    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Path to the Label Studio JSON export.",
    )

    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Path to the canonical annotated dataset.",
    )

    return parser.parse_args()


def validate_data_record(data: dict):
    missing_fields = REQUIRED_DATA_FIELDS - data.keys()

    if missing_fields:
        raise ValueError(
            f"Record {data.get('id')} is missing fields: "
            f"{sorted(missing_fields)}"
        )

    if not isinstance(data["id"], str) or not data["id"].strip():
        raise ValueError("Record id must be a non-empty string.")

    if not isinstance(data["scenario_id"], str) or not data["scenario_id"].strip():
        raise ValueError(
            f"Record {data['id']} has an invalid scenario_id."
        )

    if not isinstance(data["text"], str) or not data["text"].strip():
        raise ValueError(
            f"Record {data['id']} has empty text."
        )

    if data["language"] not in ALLOWED_LANGUAGES:
        raise ValueError(
            f"Record {data['id']} has invalid language: "
            f"{data['language']}"
        )

    if data["domain"] not in ALLOWED_DOMAINS:
        raise ValueError(
            f"Record {data['id']} has invalid domain: "
            f"{data['domain']}"
        )

    if data["source"] not in ALLOWED_SOURCES:
        raise ValueError(
            f"Record {data['id']} has invalid source: "
            f"{data['source']}"
        )


def extract_intent(task: dict) -> str:
    annotations = task.get("annotations", [])

    valid_annotations = [
        annotation
        for annotation in annotations
        if not annotation.get("was_cancelled", False)
    ]

    if len(valid_annotations) != 1:
        record_id = task.get("data", {}).get("id")

        raise ValueError(
            f"Task {record_id} must contain exactly one "
            f"non-cancelled annotation, found "
            f"{len(valid_annotations)}."
        )

    results = valid_annotations[0].get("result", [])

    intent_choices = []

    for result in results:
        if result.get("from_name") != "intent":
            continue

        choices = result.get("value", {}).get("choices", [])
        intent_choices.extend(choices)

    if len(intent_choices) != 1:
        record_id = task.get("data", {}).get("id")

        raise ValueError(
            f"Task {record_id} must contain exactly one intent "
            f"choice, found {len(intent_choices)}."
        )

    intent = intent_choices[0]

    if intent not in ALLOWED_INTENTS:
        raise ValueError(
            f"Unknown intent label: {intent}"
        )

    return intent


def main():
    args = parse_args()

    with args.input.open("r", encoding="utf-8") as file:
        tasks = json.load(file)

    if not isinstance(tasks, list):
        raise ValueError(
            "Label Studio export must contain a JSON list."
        )

    dataset = []
    seen_ids = set()

    for task in tasks:
        data = task.get("data")

        if not isinstance(data, dict):
            raise ValueError(
                "Every Label Studio task must contain a 'data' object."
            )

        validate_data_record(data)

        record_id = data["id"]

        if record_id in seen_ids:
            raise ValueError(
                f"Duplicate record id found: {record_id}"
            )

        seen_ids.add(record_id)

        intent = extract_intent(task)

        dataset.append(
            {
                "id": data["id"],
                "scenario_id": data["scenario_id"],
                "text": data["text"],
                "language": data["language"],
                "domain": data["domain"],
                "source": data["source"],
                "intent": intent,
            }
        )

    args.output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with args.output.open("w", encoding="utf-8") as file:
        json.dump(
            dataset,
            file,
            ensure_ascii=False,
            indent=2,
        )

    intent_counts = Counter(
        record["intent"]
        for record in dataset
    )

    language_counts = Counter(
        record["language"]
        for record in dataset
    )

    domain_counts = Counter(
        record["domain"]
        for record in dataset
    )

    print(f"Created {len(dataset)} annotated records")
    print(f"Output: {args.output}")

    print("\nIntent distribution:")
    for intent in sorted(intent_counts):
        print(f"  {intent}: {intent_counts[intent]}")

    print("\nLanguage distribution:")
    for language in sorted(language_counts):
        print(f"  {language}: {language_counts[language]}")

    print("\nDomain distribution:")
    for domain in sorted(domain_counts):
        print(f"  {domain}: {domain_counts[domain]}")


if __name__ == "__main__":
    main()