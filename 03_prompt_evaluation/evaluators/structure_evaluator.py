import json

def structure_score(output: str, schema: dict) -> float:
    try:
        data = json.loads(output)
        keys = schema.keys()
        matches = sum(1 for k in keys if k in data)
        return round(matches / len(keys), 2)
    except json.JSONDecodeError:
        return 0.0

if __name__ == "__main__":
    output = '{"result":"ok","confidence":"high"}'
    schema = {"result": "", "confidence": "", "notes": ""}
    print("Structure Compliance:", structure_score(output, schema))
