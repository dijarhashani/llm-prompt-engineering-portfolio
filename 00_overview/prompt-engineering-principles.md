# Prompt Engineering Principles

This document defines the **core principles** used across all prompt systems in this repository.

These principles guide prompt design, execution, and evaluation.

---

## 1. Explicit Role Definition
Every prompt must define **who the model is**.

Examples:
- Planner
- Reviewer
- Critic
- Extractor
- Decision Agent

Undefined roles lead to inconsistent behavior.

---

## 2. Task Decomposition by Default
Complex tasks are broken into **atomic steps**.

Instead of:
> “Solve this problem”

Use:
1. Understand the task
2. Identify constraints
3. Execute step-by-step
4. Validate the result

---

## 3. Output Structure Is Mandatory
Free-form output is avoided unless explicitly required.

Preferred formats:
- JSON
- Bullet lists
- Fixed schemas

Structured outputs:
- Reduce hallucinations
- Enable automated evaluation
- Improve downstream integration

---

## 4. Reasoning Control
Reasoning is **guided**, not assumed.

Prompts explicitly state:
- Whether reasoning is required
- Where it should appear
- How it should be formatted or hidden

This prevents uncontrolled chain-of-thought leakage.

---

## 5. Constraint-Driven Design
Prompts specify:
- What the model must do
- What it must not do
- How to behave when uncertain

Constraints are treated as **hard requirements**, not suggestions.

---

## 6. Refusal and Fallback Behavior
Every prompt includes:
- When to refuse
- How to refuse
- What to output instead

Silence or hallucination is never acceptable.

---

## 7. Iterative Improvement
Prompts are versioned and refined based on:
- Evaluation results
- Failure analysis
- Real-world usage patterns

Static prompts are considered incomplete.

---

## 8. Minimal Prompt Surface Area
Prompts should be:
- As short as possible
- As specific as necessary

Excess verbosity increases instability.

---

## Summary
These principles ensure that prompts behave as **reliable system components**, not unpredictable black boxes.

They are applied consistently across all modules in this repository.
