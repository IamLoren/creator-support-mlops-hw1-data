# Dataset Plan

## Dataset balance

The dataset is designed to be balanced across:

- intent;
- language;
- business domain.

The initial dataset contains:

- 9 intent classes;
- 2 languages (`uk`, `en`);
- 4 business domains.

Each semantic scenario is represented in both Ukrainian and English.

---

## Dataset Version v0.1

The first version contains one semantic scenario
for every combination of intent and business domain.

Calculation:

9 intents × 4 domains × 1 scenario × 2 languages = 72 examples.

Total:

**72 examples**

---

## Dataset Version v0.2

The second version adds one additional semantic scenario
for every combination of intent and business domain.

Calculation:

9 intents × 4 domains × 2 scenarios × 2 languages = 144 examples.

Total:

**144 examples**

---

## Future Dataset Growth

The dataset will be expanded in later project stages.

Future versions may include:

- additional manually authored examples;
- carefully reviewed synthetic examples;
- additional business domains;
- anonymized production examples.

The dataset size required for model training will be evaluated
during the model training stage.
