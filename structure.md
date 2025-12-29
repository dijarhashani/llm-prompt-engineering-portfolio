llm-prompt-engineering-portfolio/
│
├── README.md
│
├── 00_overview/
│   ├── philosophy.md
│   ├── prompt-engineering-principles.md
│   └── evaluation-criteria.md
│
├── 01_prompt_framework/
│   ├── README.md
│   ├── role_based/
│   │   ├── system_prompts.md
│   │   ├── planner_agent.md
│   │   └── critic_agent.md
│   │
│   ├── reasoning_patterns/
│   │   ├── chain_of_thought_control.md
│   │   ├── task_decomposition.md
│   │   └── self_reflection.md
│   │
│   ├── constraint_patterns/
│   │   ├── output_schema.md
│   │   ├── refusal_behavior.md
│   │   └── token_control.md
│   │
│   ├── safety_and_guardrails/
│   │   ├── prompt_injection_defense.md
│   │   ├── jailbreak_mitigation.md
│   │   └── hallucination_reduction.md
│   │
│   └── failure_cases.md
│
├── 02_prompt_execution/
│   ├── README.md
│   ├── config/
│   │   └── model_config.yaml
│   │
│   ├── runners/
│   │   ├── run_single_prompt.py
│   │   ├── run_prompt_chain.py
│   │   └── run_agent_loop.py
│   │
│   └── outputs/
│       └── sample_outputs.json
│
├── 03_prompt_evaluation/
│   ├── README.md
│   ├── metrics.md
│   ├── evaluation_rubric.md
│   │
│   ├── evaluators/
│   │   ├── accuracy_evaluator.py
│   │   ├── consistency_evaluator.py
│   │   ├── structure_evaluator.py
│   │   └── safety_evaluator.py
│   │
│   └── compare_prompts.py
│
├── 04_agents_and_workflows/
│   ├── README.md
│   ├── task_decomposition_agent/
│   │   ├── prompt.md
│   │   └── agent_flow.md
│   │
│   ├── review_agent/
│   │   ├── prompt.md
│   │   └── failure_modes.md
│   │
│   └── memory_patterns.md
│
├── 05_domain_case_studies/
│   ├── README.md
│   ├── code_review_ai/
│   │   ├── problem.md
│   │   ├── constraints.md
│   │   ├── prompt_versions.md
│   │   ├── evaluation_results.md
│   │   └── final_prompt.md
│   │
│   └── business_strategy_ai/
│       ├── problem.md
│       ├── prompt_design.md
│       ├── risks.md
│       └── final_prompt.md
│
├── 06_prompt_security_lab/
│   ├── README.md
│   ├── attack_prompts.md
│   ├── defense_patterns.md
│   └── red_team_vs_blue_team.md
│
├── 07_reproducibility/
│   ├── environment.md
│   ├── requirements.txt
│   └── setup.py
│
└── 08_appendix/
    ├── glossary.md
    ├── references.md
    └── roadmap.md
