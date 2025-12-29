import json

def planner(task: str) -> dict:
    return {
        "goal": task,
        "steps": [
            "Analyze task",
            "Execute solution",
            "Review output"
        ]
    }

def executor(plan: dict) -> dict:
    return {
        "execution": "Mock execution based on plan",
        "steps_executed": plan["steps"]
    }

def critic(output: dict) -> dict:
    return {
        "issues": [],
        "assessment": "Output meets requirements"
    }


if __name__ == "__main__":
    task = "Evaluate risks of prompt injection"
    
    plan = planner(task)
    execution = executor(plan)
    review = critic(execution)

    result = {
        "plan": plan,
        "execution": execution,
        "review": review
    }

    print(json.dumps(result, indent=2))
