def calculate(expression: str) -> float:
    if not expression:
        return 0
    if len(expression) == 1:
        return float(expression)
    return float(expression[0]) + float(expression[-1])

