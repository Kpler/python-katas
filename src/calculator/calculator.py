def calculate(expression: str) -> float:
    if not expression:
        return 0
    first_number = get_first_number(expression)
    next_expr_start_index = len(first_number) + 3
    next_expr = expression[next_expr_start_index:]
    if not next_expr:
        return float(first_number)
    operator = expression[len(first_number) + 1]
    if operator == "+":
        return float(first_number) + calculate(next_expr)
    elif operator == "-":
        return float(first_number) - calculate(next_expr)


def get_first_number(expression: str) -> str:
    return expression.split(" ")[0]

