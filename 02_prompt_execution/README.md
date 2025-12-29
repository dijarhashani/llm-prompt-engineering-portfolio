# Prompt Execution Layer

This directory contains the **execution layer** for running prompt frameworks
against LLM APIs in a controlled and reproducible way.

The goal of this layer is **not** to abstract prompts away,
but to **execute, chain, and test them as systems**.

---

## Design Goals

- Minimal infrastructure
- Clear execution flow
- Reproducible runs
- Separation between prompts and code

This layer intentionally avoids:
- Heavy frameworks
- Agent libraries
- Hidden prompt logic

---

## Components

- `config/` → Model and runtime configuration
- `runners/` → Execution scripts
- `outputs/` → Sample and reference outputs

---

## Execution Philosophy

Python is used here as a **runner and**
