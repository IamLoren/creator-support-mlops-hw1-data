import json
from pathlib import Path


RAW_DATA_PATH = Path("data/raw/customer_support_messages_v0.1.json")
OUTPUT_PATH = Path("annotation/label_studio_tasks_v0.1.json")


with RAW_DATA_PATH.open("r", encoding="utf-8") as file:
    records = json.load(file)


tasks = [{"data": record} for record in records]


with OUTPUT_PATH.open("w", encoding="utf-8") as file:
    json.dump(
        tasks,
        file,
        ensure_ascii=False,
        indent=2,
    )


print(f"Created {len(tasks)} Label Studio tasks")
print(f"Saved to: {OUTPUT_PATH}")