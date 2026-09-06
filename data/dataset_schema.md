# Dataset Schema

## Overview

The dataset contains bilingual Ukrainian and English customer-support
messages for Creator and SMB use cases.

Each record represents one incoming customer message.

The raw dataset does not contain an intent label.
The intent is added during manual annotation in Label Studio.

---

## Raw Dataset Schema

Each raw example contains the following fields:

### `id`

Unique identifier of the dataset example.

Example:

`uk_education_0001`

The ID must be unique across the whole dataset.

---

### `scenario_id`

Identifier of the semantic scenario represented by the message.

It is used to group Ukrainian and English examples that represent
the same or nearly identical customer-support situation.

Example:

Ukrainian:

`scenario_id: schedule_001`

> "Коли буде наступний вебінар?"

English:

`scenario_id: schedule_001`

> "When is the next webinar?"

Keeping the same `scenario_id` will later help prevent data leakage
when the dataset is split into train, validation, and test sets.

---

### `text`

The actual customer message.

Examples:

> "Не можу відкрити третій урок."

> "I can't open the third lesson."

---

### `language`

Language of the message.

Allowed values:

- `uk`
- `en`

---

### `domain`

Business domain represented by the example.

Allowed values:

- `education`
- `fitness`
- `beauty`
- `professional_services`

The field is metadata and is not the prediction target.

It will later allow us to evaluate model quality separately
for different business domains.

---

### `source`

Origin of the example.

Possible values:

- `manual` — manually authored example;
- `synthetic` — synthetically generated example;
- `production_anonymized` — anonymized real production example.

For Homework 1, only non-production data will be used.

---

## Annotated Dataset Schema

After manual annotation, each record contains all fields from the raw
dataset plus the following field:

### `intent`

The manually assigned customer-support intent.

Allowed values:

- `ACCESS_ACCOUNT`
- `SCHEDULE_DEADLINE`
- `CONTENT_USAGE_QUESTION`
- `SERVICE_INFO`
- `TECHNICAL_ISSUE`
- `CHANGE_CANCEL`
- `FEEDBACK_COMPLAINT`
- `HUMAN_SUPPORT`
- `OTHER`

Each message must have exactly one intent.

---

## Initial Business Domains

The first dataset version covers four business domains:

### `education`

Examples related to online courses, educational programs,
lessons, assignments, webinars, and learning materials.

### `fitness`

Examples related to training programs, workouts,
fitness coaching, schedules, and exercise instructions.

### `beauty`

Examples related to beauty services, cosmetology,
appointments, procedures, and aftercare instructions.

### `professional_services`

Examples related to consulting, legal, accounting,
agency, and other professional services.

---

## Identifier Naming Rules

### Example `id`

Each dataset record must have a unique `id`.

Format:

`<language>_<domain>_<number>`

Examples:

- `uk_education_0001`
- `en_education_0001`
- `uk_fitness_0001`
- `en_beauty_0012`

Rules:

- `language` must be either `uk` or `en`;
- `domain` must be one of the allowed business domains;
- the numeric part must contain four digits;
- every record must have a unique `id`.

---

### `scenario_id`

`scenario_id` identifies one semantic customer-support situation.

Format:

`<domain>_<intent_short_name>_<number>`

Examples:

- `education_access_001`
- `fitness_technical_001`
- `beauty_schedule_002`
- `professional_services_change_001`

Ukrainian and English examples that represent the same semantic
scenario must use the same `scenario_id`.

Example:

Ukrainian:

`id: uk_education_0001`

English:

`id: en_education_0001`

Both:

`scenario_id: education_access_001`

This makes it possible to keep semantically equivalent bilingual
examples together during future train/validation/test splitting.
