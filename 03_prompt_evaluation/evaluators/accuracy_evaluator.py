def accuracy_score(output: str, reference: str) -> float:
    output_tokens = set(output.lower().split())
    reference_tokens = set(reference.lower().split())
    match = output_tokens & reference_tokens
    score = len(match) / max(len(reference_tokens), 1)
    return round(score, 2)

if __name__ == "__main__":
    output = "The system risks hallucinations and injections."
    reference = "The system risks prompt injection and hallucinations."
    print("Accuracy:", accuracy_score(output, reference))
