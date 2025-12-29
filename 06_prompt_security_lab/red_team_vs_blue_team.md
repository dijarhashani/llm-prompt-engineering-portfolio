# Red Team vs Blue Team Exercises

This document demonstrates **simulated security testing** for prompts.

---

## Red Team (Attacker)
- Attempts to break prompt safety
- Uses attack patterns:
  - Prompt injection
  - Role confusion
  - Malicious chaining

### Example Task
- Red Team tries to make the model output sensitive instructions
- Observes success/failure

---

## Blue Team (Defender)
- Implements defense patterns
- Monitors model responses
- Adjusts system prompts to mitigate attacks

### Example Strategy
- Enforce instruction hierarchy
- Explicit refusal conditions
- Validate JSON outputs
- Log any attempted violations

---

## Lab Procedure
1. Select a target prompt
2. Red Team crafts attacks
3. Blue Team applies defenses
4. Run multiple iterations
5. Document results and iterate

---

## Goals
- Identify weaknesses in prompts
- Improve robustness of workflows
- Demonstrate **senior-level security awareness**
