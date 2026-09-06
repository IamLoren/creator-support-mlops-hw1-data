# Scenario Catalog

## Purpose

This file defines the semantic scenarios used to build dataset version `v0.1`.

Dataset version `v0.1` contains:

- 9 intent classes;
- 4 business domains;
- 1 scenario for each intent × domain combination;
- 2 language variants for each scenario (`uk` and `en`).

Total:

36 semantic scenarios × 2 languages = 72 dataset examples.

The scenario catalog is a dataset design document.
The intended intent is documented here, but it is not included
in the raw dataset imported into Label Studio.

---

## Dataset v0.1 Scenarios

| Scenario ID | Domain | Intended Intent | Scenario |
|---|---|---|---|
| `education_access_001` | education | ACCESS_ACCOUNT | Customer paid for a course but cannot access it |
| `fitness_access_001` | fitness | ACCESS_ACCOUNT | Customer purchased a training program but cannot see it in the account |
| `beauty_access_001` | beauty | ACCESS_ACCOUNT | Customer should have access to aftercare materials but they are unavailable |
| `professional_services_access_001` | professional_services | ACCESS_ACCOUNT | Customer cannot access documents or materials shared after a consultation |
| `education_schedule_001` | education | SCHEDULE_DEADLINE | Customer asks when the next webinar starts |
| `fitness_schedule_001` | fitness | SCHEDULE_DEADLINE | Customer asks when the next scheduled training session takes place |
| `beauty_schedule_001` | beauty | SCHEDULE_DEADLINE | Customer asks what time a beauty appointment is scheduled |
| `professional_services_schedule_001` | professional_services | SCHEDULE_DEADLINE | Customer asks about the deadline or time of an upcoming consultation |
| `education_content_001` | education | CONTENT_USAGE_QUESTION | Customer does not understand how to complete an exercise from a lesson |
| `fitness_content_001` | fitness | CONTENT_USAGE_QUESTION | Customer asks how many repetitions of an exercise should be performed |
| `beauty_content_001` | beauty | CONTENT_USAGE_QUESTION | Customer asks how to follow an aftercare instruction |
| `professional_services_content_001` | professional_services | CONTENT_USAGE_QUESTION | Customer asks how to use a provided template or document |
| `education_service_001` | education | SERVICE_INFO | Customer asks what is included in a course |
| `fitness_service_001` | fitness | SERVICE_INFO | Customer asks what is included in a coaching or training package |
| `beauty_service_001` | beauty | SERVICE_INFO | Customer asks what is included in a beauty service or procedure |
| `professional_services_service_001` | professional_services | SERVICE_INFO | Customer asks what is included in a consulting service |
| `education_technical_001` | education | TECHNICAL_ISSUE | Course video is accessible but does not play |
| `fitness_technical_001` | fitness | TECHNICAL_ISSUE | Workout PDF or file cannot be downloaded |
| `beauty_technical_001` | beauty | TECHNICAL_ISSUE | Booking or aftercare page produces a technical error |
| `professional_services_technical_001` | professional_services | TECHNICAL_ISSUE | Customer portal feature or uploaded document does not work correctly |
| `education_change_001` | education | CHANGE_CANCEL | Customer asks to extend an assignment deadline |
| `fitness_change_001` | fitness | CHANGE_CANCEL | Customer asks to reschedule a coaching session |
| `beauty_change_001` | beauty | CHANGE_CANCEL | Customer asks to reschedule or cancel an appointment |
| `professional_services_change_001` | professional_services | CHANGE_CANCEL | Customer asks to change or cancel a consultation |
| `education_feedback_001` | education | FEEDBACK_COMPLAINT | Customer gives positive or negative feedback about a course |
| `fitness_feedback_001` | fitness | FEEDBACK_COMPLAINT | Customer comments on their experience with the training program |
| `beauty_feedback_001` | beauty | FEEDBACK_COMPLAINT | Customer expresses satisfaction or dissatisfaction with the service |
| `professional_services_feedback_001` | professional_services | FEEDBACK_COMPLAINT | Customer gives feedback about consulting or professional support |
| `education_human_001` | education | HUMAN_SUPPORT | Customer explicitly asks to speak with a human support agent or tutor |
| `fitness_human_001` | fitness | HUMAN_SUPPORT | Customer explicitly requests contact with a trainer or support person |
| `beauty_human_001` | beauty | HUMAN_SUPPORT | Customer asks to speak with a salon representative or manager |
| `professional_services_human_001` | professional_services | HUMAN_SUPPORT | Customer explicitly asks to speak with a consultant or manager |
| `education_other_001` | education | OTHER | Customer sends a message unrelated to the educational service |
| `fitness_other_001` | fitness | OTHER | Customer sends an unrelated message to the fitness business |
| `beauty_other_001` | beauty | OTHER | Customer asks something unrelated to the beauty service |
| `professional_services_other_001` | professional_services | OTHER | Customer sends an unrelated or meaningless message |
