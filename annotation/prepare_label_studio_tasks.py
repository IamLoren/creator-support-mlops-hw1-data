import argparse
import json
from pathlib import Path


REQUIRED_FIELDS = {
    "id",
    "scenario_id",
    "text",
    "language",
    "domain",
    "source",
}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Prepare raw customer-support records for Label Studio."
    )

    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Path to the raw JSON dataset.",
    )

    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Path where Label Studio tasks will be written.",
    )

    return parser.parse_args()


def validate_record(record: dict):
    missing_fields = REQUIRED_FIELDS - record.keys()

    if missing_fields:
        raise ValueError(
            f"Record {record.get('id')} is missing fields: "
            f"{sorted(missing_fields)}"
        )

    if "intent" in record:
        raise ValueError(
            f"Raw record {record['id']} already contains an intent label."
        )


def main():
    args = parse_args()

    with args.input.open("r", encoding="utf-8") as file:
        records = json.load(file)

    if not isinstance(records, list):
        raise ValueError("Input JSON must contain a list of records.")

    tasks = []

    for record in records:
        validate_record(record)

        tasks.append(
            {
                "data": record
            }
        )

    args.output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with args.output.open("w", encoding="utf-8") as file:
        json.dump(
            tasks,
            file,
            ensure_ascii=False,
            indent=2,
        )

    print(f"Created {len(tasks)} Label Studio tasks")
    print(f"Input:  {args.input}")
    print(f"Output: {args.output}")


if __name__ == "__main__":
    main()