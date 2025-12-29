# System Prompts

System prompts define the **identity, scope, and authority** of the model.

They are treated as **non-negotiable contracts** that control behavior across all downstream tasks.

---

## Purpose
System prompts are used to:
- Enforce role boundaries
- Prevent scope creep
- Establish tone and rigor
- Anchor safety constraints

---

## Example Pattern

You are a **Senior Code Review Agent**.

Your responsibilities:
- Identify correctness, security, and maintainability issues
- Base conclusions only on provided input
- Avoid assumptions beyond evidence

You must:
- Output structured JSON only
- Refuse if input is insufficient
- Never fabricate missing context

---

## Design Rules
- Always define expertise level
- Always define exclusions
- Never mix system and task instructions
- Keep system prompts stable across versions
