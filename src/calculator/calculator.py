def calculate(expression: str) -> float:
    split_expression = expression.split(" ")

    sum = 0
    for n in split_expression:
        if n.isdigit():
            sum += float(n)
    return sum
