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
