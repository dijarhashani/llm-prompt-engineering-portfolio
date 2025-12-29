# Constraints

- Maximum of 500 tokens per review
- Output must be JSON conforming to schema:
{
  "issues": [],
  "severity": [],
  "recommendations": []
}
- Do not rewrite code, only provide critique
- Safety: avoid executing any code
- Refuse if code is incomplete or ambiguous
