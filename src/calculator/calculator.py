def calculate(expression: str) -> float:
    split = expression.split(" ")
    nextOperator = "+"
    value = 0
    for element in split:

        if nextOperator == "+":
            value += float(element)
        else:
            value -= float(element)

    return value
