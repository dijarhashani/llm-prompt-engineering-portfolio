def consistency_score(outputs: list) -> float:
    if not outputs:
        return 0.0
    reference = outputs[0]
    matches = sum(1 for o in outputs if o == reference)
    return round(matches / len(outputs), 2)


if __name__ == "__main__":
    runs = [
        "Step A completed, output valid.",
        "Step A completed, output valid.",
        "Step A completed, output valid."
    ]
    print("Consistency:", consistency_score(runs))
