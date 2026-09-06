# Annotation Guidelines

## Purpose

This document defines the annotation rules for the
Ukrainian-English Creator & SMB Customer Support Intent Dataset.

Each customer message must be assigned exactly one intent label.

The same annotation rules must be applied to both Ukrainian and English messages.

## General annotation rules

1. Assign exactly one intent to each message.
2. Choose the intent based on the user's primary goal, not only on individual keywords.
3. Use the same rules for Ukrainian and English examples.
4. If a message could belong to multiple classes, choose the class representing the main user request.
5. If none of the defined intents fits the message, use `OTHER`.
6. Ambiguous cases should be documented and used to improve these guidelines.

---

## 1. ACCESS_ACCOUNT

### Definition

Use `ACCESS_ACCOUNT` when the user's main problem is related to authentication,
account access, permissions, or access to purchased/assigned content.

### Positive examples

Ukrainian:

- "Не можу увійти у свій акаунт."
- "Після оплати мені не відкрився доступ до курсу."
- "Система пише, що в мене немає доступу до матеріалів."

English:

- "I can't log into my account."
- "I paid for the course but I still don't have access."
- "It says I don't have permission to view the materials."

### Permission-related errors

Use `ACCESS_ACCOUNT` when the message indicates that access is denied because of
permissions or authorization, including errors such as:

- `403 Forbidden`;
- "Access denied";
- "You don't have permission";
- content marked as unavailable for the current user.

Example:

> "Сайт відкривається, але другий модуль показує 403 Forbidden."

Classification:

`ACCESS_ACCOUNT`

### Do not use when

Do not use `ACCESS_ACCOUNT` if the user successfully has access to the platform
or content, but a particular technical feature does not work.

Example:

> "Я відкрив урок, але відео не запускається."

This should be classified as:

`TECHNICAL_ISSUE`

### Boundary rule

Use:

- `ACCESS_ACCOUNT` → the user **cannot gain access**
- `TECHNICAL_ISSUE` → the user **has access, but something does not work correctly**

---

## 2. TECHNICAL_ISSUE

### Definition

Use `TECHNICAL_ISSUE` when the user can access the platform, account, service, or content,
but a technical component does not work correctly.

Typical technical issues include problems with:

- video playback;
- file downloading;
- broken buttons or links;
- page loading;
- application errors;
- unexpected system behavior.

### Positive examples

Ukrainian:

- "Відео в третьому уроці не запускається."
- "Не можу завантажити PDF."
- "Кнопка «Зберегти» не працює."
- "Сторінка постійно показує помилку."

English:

- "The video in lesson three won't play."
- "I can't download the PDF."
- "The Save button doesn't work."
- "The page keeps showing an error."

### Do not use when

Do not use `TECHNICAL_ISSUE` when the main problem is that the user does not have
permission or access to the account, course, service, or materials.

Do not use `TECHNICAL_ISSUE` for explicit authentication, authorization, or
permission errors such as `401 Unauthorized` or `403 Forbidden`.

Example:

> "Пише, що в мене немає доступу до курсу."

This should be classified as:

`ACCESS_ACCOUNT`

### Boundary rule

Use:

- `ACCESS_ACCOUNT` → the user cannot access the account, service, or content;
- `TECHNICAL_ISSUE` → the user has access, but a technical feature or resource does not work correctly.

---

## 3. SCHEDULE_DEADLINE

### Definition

Use `SCHEDULE_DEADLINE` when the user's main request is about:

- date;
- time;
- schedule;
- deadline;
- duration;
- start or end time of an event;
- when something will happen or must be completed.

### Positive examples

Ukrainian:

- "Коли буде наступний вебінар?"
- "До якого числа потрібно здати домашнє завдання?"
- "О котрій починається консультація?"
- "Скільки ще буде відкритий доступ до цього модуля?"

English:

- "When is the next webinar?"
- "What is the deadline for the assignment?"
- "What time does the consultation start?"
- "How long will this module remain available?"

### Do not use when

Do not use `SCHEDULE_DEADLINE` if the user's main goal is to change or cancel an existing booking or event.

Example:

> "Можна перенести консультацію на п'ятницю?"

This should be classified as:

`CHANGE_CANCEL`

Do not use `SCHEDULE_DEADLINE` if the user is asking general information about the service rather than a specific date, time, or deadline.

Example:

> "Скільки триває весь курс?"

Depending on the dataset rules, this should usually be classified as:

`SERVICE_INFO`

### Boundary rule

Use:

- `SCHEDULE_DEADLINE` → the user wants to know **when** something happens, starts, ends, or must be completed;
- `CHANGE_CANCEL` → the user wants to **modify or cancel** an existing schedule, booking, appointment, or service;
- `SERVICE_INFO` → the user asks general descriptive information about the service or product.
