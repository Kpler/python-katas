def calculate(expression: str) -> float:
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
