import json

def run_prompt_chain(prompts: list) -> dict:
    chain_results = []

    for step, prompt in enumerate(prompts, start=1):
        output = {
            "step": step,
            "prompt": prompt,
            "response": f"Mock response for step {step}"
        }
        chain_results.append(output)

    return {
        "chain_length": len(prompts),
        "results": chain_results
    }


if __name__ == "__main__":
    prompts = [
        "Understand the task and constraints.",
        "Generate a solution.",
        "Validate the solution."
    ]

    result = run_prompt_chain(prompts)
    print(json.dumps(result, indent=2))
