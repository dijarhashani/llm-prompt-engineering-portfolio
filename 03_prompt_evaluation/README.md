# Prompt Evaluation

This directory contains the **evaluation layer** for measuring
the effectiveness of prompts as systems.

Evaluation is **mandatory at senior level**, ensuring prompts are:
- Accurate
- Consistent
- Structured
- Safe
- Reproducible

---

## Components

- `metrics.md` → Definitions of evaluation metrics
- `evaluation_rubric.md` → Rubric for scoring prompts
- `evaluators/` → Python scripts implementing metric evaluations
- `compare_prompts.py` → Script to compare multiple prompt versions

---

## Evaluation Philosophy

1. Treat prompts as **system components**, not text.
2. Measure outcomes **objectively**.
3. Track **failures** to improve design.
4. Separate metrics by **type** (accuracy, structure, safety, consiste
