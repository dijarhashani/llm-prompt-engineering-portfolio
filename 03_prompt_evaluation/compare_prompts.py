from evaluators.accuracy_evaluator import accuracy_score
from evaluators.consistency_evaluator import consistency_score
from evaluators.structure_evaluator import structure_score
from evaluators.safety_evaluator import safety_score

prompts = ["Prompt A", "Prompt B"]
outputs = [
    '{"result":"ok","confidence":"high"}',
    '{"result":"ok","confidence":"medium"}'
]
reference = "ok high"
schema = {"result": "", "confidence": ""}
unsafe_terms = ["hack", "bypass", "override"]

for i, output in enumerate(outputs):
    print(f"Prompt {i+1} Evaluation:")
    print("Accuracy:", accuracy_score(output, reference))
    print("Structure:", structure_score(output, schema))
    print("Safety:", safety_score(output, unsafe_terms))
    print("-" * 40)
