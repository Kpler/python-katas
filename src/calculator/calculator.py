def calculate(expression: str) -> float:
    split_expression = expression.split(" ")
    if '+' in split_expression:
        return float(split_expression[0]) + float(split_expression[2])
    else:
        return 0
