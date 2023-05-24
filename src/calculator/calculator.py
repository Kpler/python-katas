def calculate(expression: str) -> float:
    value = 1
    if "*" in expression:
        for element in expression.split(" * "):
            value *= calculate(element)
        return value

    operator_list = ["+", "-", "*"]
    next_operator = "+"
    value = 0
    for element in expression.split(" "):
        if element in operator_list:
            next_operator = element
            continue

        if next_operator == "+":
            value += float(element)
        elif next_operator == "-":
            value -= float(element)
        else:
            value *= float(element)

    return value
