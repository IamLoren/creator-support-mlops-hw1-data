import json
from pathlib import Path


EXPORT_PATH = Path(
    "annotation/exports/label_studio_export_v0.1.json"
)

OUTPUT_PATH = Path(
    "data/annotated/customer_support_intents.json"
)


REQUIRED_FIELDS = {
    "id",
    "scenario_id",
    "text",
    "language",
    "domain",
    "source",
}


ALLOWED_INTENTS = {
    "ACCESS_ACCOUNT",
    "SCHEDULE_DEADLINE",
    "CONTENT_USAGE_QUESTION",
    "SERVICE_INFO",
    "TECHNICAL_ISSUE",
    "CHANGE_CANCEL",
    "FEEDBACK_COMPLAINT",
    "HUMAN_SUPPORT",
    "OTHER",
}


def extract_intent(task: dict) -> str:
    """Extract exactly one manually assigned intent from a Label Studio task."""

    annotations = [
        annotation
        for annotation in task.get("annotations", [])
        if not annotation.get("was_cancelled", False)
    ]

    if len(annotations) != 1:
        raise ValueError(
            f"Task {task.get('id')} must have exactly one annotation, "
            f"found {len(annotations)}"
        )

    intent_results = []

    for result in annotations[0].get("result", []):
        if (
            result.get("from_name") == "intent"
            and result.get("type") == "choices"
        ):
            choices = result.get("value", {}).get("choices", [])

            if len(choices) != 1:
                raise ValueError(
                    f"Task {task.get('id')} must contain exactly one intent choice"
                )

            intent_results.append(choices[0])

    if len(intent_results) != 1:
        raise ValueError(
            f"Task {task.get('id')} must contain exactly one intent result"
        )

    intent = intent_results[0]

    if intent not in ALLOWED_INTENTS:
        raise ValueError(
            f"Unexpected intent '{intent}' in task {task.get('id')}"
        )

    return intent


with EXPORT_PATH.open("r", encoding="utf-8") as file:
    tasks = json.load(file)


records = []
seen_ids = set()


for task in tasks:
    data = task.get("data", {})

    missing_fields = REQUIRED_FIELDS - data.keys()

    if missing_fields:
        raise ValueError(
            f"Task {task.get('id')} is missing fields: "
            f"{sorted(missing_fields)}"
        )

    record_id = data["id"]

    if record_id in seen_ids:
        raise ValueError(
            f"Duplicate dataset ID: {record_id}"
        )

    seen_ids.add(record_id)

    intent = extract_intent(task)

    record = {
        "id": data["id"],
        "scenario_id": data["scenario_id"],
        "text": data["text"],
        "language": data["language"],
        "domain": data["domain"],
        "source": data["source"],
        "intent": intent,
    }

    records.append(record)


OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

with OUTPUT_PATH.open("w", encoding="utf-8") as file:
    json.dump(
        records,
        file,
        ensure_ascii=False,
        indent=2,
    )


print(f"Created {len(records)} annotated records")
print(f"Saved to: {OUTPUT_PATH}")