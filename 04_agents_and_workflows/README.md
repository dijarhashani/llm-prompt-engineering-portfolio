# Agents and Workflows

This directory demonstrates **how prompt patterns are orchestrated into multi-step agent workflows**.

Key principles:

1. **Agents are roles** (Planner, Executor, Critic, Reviewer)  
2. **Workflows are sequences of prompts** executed systematically  
3. **Memory patterns** enable context retention across steps  
4. **Failures are analyzed and tracked**  

---

## Structure

- `task_decomposition_agent/` → Breaks complex tasks into atomic steps  
- `review_agent/` → Evaluates outputs and identifies failures  
- `memory_patterns.md` → Defines memory and context handling strategies

This layer bridges **prompt design** and **execution**, creating reproducible, agent-driven systems.
