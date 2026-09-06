# Creator Support MLOps — HW1: Data Management

## Project goal

The goal of this project is to prepare and version a bilingual dataset
for training a machine learning model that classifies incoming customer
support messages by user intent.

The dataset will later be used to build an AI Customer Support Router
for creators and small and medium-sized businesses (SMBs).

Future homework stages will reuse this dataset for model training,
inference, and monitoring.

## Machine Learning Task

The ML task is **multiclass text classification**.

### Input

A customer support message written in Ukrainian or English.

Example:

> "Не можу відкрити третій урок."

### Output

One intent class describing what the customer wants or what problem
they are reporting.

Example:

> `TECHNICAL_ISSUE`

## Languages

The dataset supports two languages from the beginning:

- Ukrainian (`uk`)
- English (`en`)

This is important because the future product is planned for both
Ukrainian and international users.

## Dataset

The project uses a custom dataset:

**Ukrainian-English Creator & SMB Customer Support Intent Dataset**

The first version of the dataset contains customer support messages
from several business domains and is manually annotated using
Label Studio.

## Initial intent classes

1. `ACCESS_ACCOUNT`
2. `SCHEDULE_DEADLINE`
3. `CONTENT_USAGE_QUESTION`
4. `SERVICE_INFO`
5. `TECHNICAL_ISSUE`
6. `CHANGE_CANCEL`
7. `FEEDBACK_COMPLAINT`
8. `HUMAN_SUPPORT`
9. `OTHER`

## Homework 1 scope

This homework covers:

- dataset design;
- data annotation;
- dataset versioning;
- remote dataset storage.

Model training is not part of Homework 1.

## Labeling tool

Annotation is done with **Label Studio**.

Key project files:

- labeling config: `annotation/labeling_config.xml`
- annotation guidelines: `annotation/annotation_guidelines.md`
- Label Studio tasks (v0.1): `annotation/label_studio_tasks_v0.1.json`
- Label Studio tasks (batch 002 / v0.2): `annotation/label_studio_tasks_batch_002.json`
- Label Studio exports: `annotation/exports/`

## Setup

Use **Python 3.10–3.12** (Label Studio is not compatible with Python 3.14).

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash
# .venv\Scripts\activate        # Windows PowerShell
# source .venv/bin/activate     # Linux / macOS

pip install -r requirements.txt
```

## How to start / open annotation

1. Start Label Studio:

```bash
label-studio start
```

2. Open `http://localhost:8080` in the browser.
3. Create a new project.
4. Paste the labeling config from `annotation/labeling_config.xml`.
5. Import tasks, for example:

- `annotation/label_studio_tasks_v0.1.json` for dataset v0.1
- `annotation/label_studio_tasks_batch_002.json` for the second batch used in v0.2

6. Annotate messages using the rules in `annotation/annotation_guidelines.md`.
7. Export annotations in JSON format into `annotation/exports/`.

You should see the same labeling system with 9 intent labels.

## Reproduce the canonical dataset

The canonical annotated dataset path is:

`data/annotated/customer_support_intents.json`

Rebuild it from a versioned Label Studio export:

```bash
python scripts/build_annotated_dataset.py \
  --input annotation/exports/label_studio_export_v0.2.json \
  --output data/annotated/customer_support_intents.json
```

Expected result: `144 annotated records`.

Validate the dataset:

```bash
python scripts/validate_dataset.py \
  --input data/annotated/customer_support_intents.json \
  --expected-records 144 \
  --expected-scenarios 72
```

Expected result: `Dataset validation PASSED`.

For dataset v0.1, use:

```bash
python scripts/build_annotated_dataset.py \
  --input annotation/exports/label_studio_export_v0.1.json \
  --output data/annotated/customer_support_intents.json

python scripts/validate_dataset.py \
  --input data/annotated/customer_support_intents.json \
  --expected-records 72 \
  --expected-scenarios 36
```

## Dataset Versions

### v0.1

- 72 annotated messages
- 36 semantic scenarios
- 2 languages: Ukrainian and English
- 4 business domains
- 9 intent classes
- 8 examples per intent

Git tag: `dataset-v0.1`

### v0.2

- 144 annotated messages
- 72 semantic scenarios
- 2 languages: Ukrainian and English
- 4 business domains
- 9 intent classes
- 16 examples per intent

Git tag: `dataset-v0.2`

The canonical annotated dataset uses a stable logical path:

`data/annotated/customer_support_intents.json`

Dataset content is versioned with DVC. Git commits and tags identify dataset releases.

## How dataset versioning works

1. Annotate data in Label Studio and export JSON.
2. Build the canonical file with `scripts/build_annotated_dataset.py`.
3. Validate with `scripts/validate_dataset.py`.
4. Track the canonical file with DVC.
5. Commit Git metadata (`.dvc` file + related project files).
6. Tag the release (`dataset-v0.1`, `dataset-v0.2`).
7. Push dataset content to the DVC remote (Cloudflare R2).

To inspect a release snapshot:

```bash
git checkout dataset-v0.1
git checkout dataset-v0.2
```

Each tag points to the corresponding DVC metadata for that dataset release.

The DVC remote is a private Cloudflare R2 bucket. Remote access requires
authorized credentials, which are not stored in the repository.

The canonical dataset can also be reproduced locally from the versioned
Label Studio export using `build_annotated_dataset.py`.

## Data Lineage

Raw messages → Label Studio → manual annotation → Label Studio export → canonical dataset → validation → DVC → Cloudflare R2
