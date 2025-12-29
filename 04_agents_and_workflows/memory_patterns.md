# Memory Patterns for Multi-Agent Workflows

Memory is required to maintain **context across steps and agents**.

---

## Types of Memory

1. **Short-term Memory**
   - Current task context
   - Intermediate outputs
   - Discarded after workflow completes

2. **Long-term Memory**
   - Agent learning and improvements
   - Frequently referenced knowledge
   - Versioned and auditable

---

## Best Practices

- Store memory in structured formats (JSON, database)
- Reference memory explicitly in prompts
- Limit token size for LLM efficiency
- Track updates and revisions
- Ensure sensitive data is redacted

---

## Use in Workflows

- Task Decomposition Agent references prior steps
- Review Agent checks outputs against memory
- Chains and agents maintain continuity without hallucination
