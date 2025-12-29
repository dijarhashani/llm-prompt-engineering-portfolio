# Output Schema Constraint

This pattern enforces strict output formats.

---

## Benefits
- Machine readability
- Evaluation automation
- Reduced ambiguity

---

## Example

Output JSON only.

Schema:
{
  "result": "",
  "confidence": "",
  "notes": ""
}

---

## Failure Handling
If schema cannot be satisfied, refuse with explanation.
