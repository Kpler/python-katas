def calculate(expression: str) -> float:
    tokens = expression.split()

    for token in tokens:
        calculate(token)
    return tokens
