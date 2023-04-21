def calculate(expression: str) -> float:
    if not expression:
        return 0
    return get_first_number(expression) + calculate(expression[4:])


def get_first_number(expression: str) -> float:
    operator = "+"
    print(float(expression.replace(" ", "").split(operator)))
    return float(expression.replace(" ", "").split(operator)[0])

