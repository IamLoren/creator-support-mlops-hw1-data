# Creator Support MLOps — HW1: Data Management

## Project goal

The goal of this project is to prepare and version a bilingual dataset
for training a machine learning model that classifies incoming customer
support messages by user intent.

The dataset will later be used to build an AI Customer Support Router
for creators and small and medium-sized businesses (SMBs).

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

The first version of the dataset will contain customer support messages
from several business domains and will be manually annotated using
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
