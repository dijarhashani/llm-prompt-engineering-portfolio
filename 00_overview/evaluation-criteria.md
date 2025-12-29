# Prompt Evaluation Criteria

This document defines how prompt quality is **measured objectively** in this repository.

Prompts are evaluated as **systems**, not as isolated responses.

---

## 1. Accuracy
**Definition:**  
Does the output correctly address the task?

**Evaluation signals:**
- Factual correctness
- Logical validity
- Task completion

**Failure indicators:**
- Incorrect conclusions
- Fabricated facts
- Partial task execution

---

## 2. Consistency
**Definition:**  
Does the prompt produce similar outputs across multiple runs?

**Evaluation signals:**
- Stable structure
- Predictable reasoning paths
- Low variance in output format

**Failure indicators:**
- Output drift
- Structural inconsistency
- Random formatting changes

---

## 3. Output Structure Compliance
**Definition:**  
Does the output match the expected format exactly?

**Evaluation signals:**
- Schema validity
- Field completeness
- Correct data types

**Failure indicators:**
- Missing fields
- Invalid JSON
- Mixed free-form text

---

## 4. Constraint Adherence
**Definition:**  
Does the model respect explicit instructions and limitations?

**Evaluation signals:**
- Obedience to role
- Respect for exclusions
- Proper refusal behavior

**Failure indicators:**
- Ignoring constraints
- Overstepping scope
- Hallucinated additions

---

## 5. Safety and Risk Handling
**Definition:**  
Does the prompt prevent unsafe or unintended behavior?

**Evaluation signals:**
- Resistance to prompt injection
- Controlled refusal
- No sensitive data leakage

**Failure indicators:**
- Jailbreak success
- Unsafe compliance
- Overconfident hallucinations

---

## 6. Explainability (When Required)
**Definition:**  
Is the output understandable and justifiable when explanations are requested?

**Evaluation signals:**
- Clear reasoning
- Step traceability
- Justified decisions

**Failure indicators:**
- Opaque logic
- Contradictions
- Unsupported claims

---

## 7. Cost and Efficiency (Optional)
**Definition:**  
Does the prompt achieve results efficiently?

**Evaluation signals:**
- Token usage
- Prompt length
- Execution time

Used when cost or latency is a constraint.

---

## Summary
A prompt is considered **production-ready** only when it:
- Meets accuracy requirements
- Behaves consistently
- Respects constraints
- Is evaluatable and reproducible
- Handles failure safely

Anything less is experimental.
