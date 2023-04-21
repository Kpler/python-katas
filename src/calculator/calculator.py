
def calculate(expression: str) -> float:
    if not expression:
        return 0
    first_number = get_first_number(expression)
    next_expr = get_next_expression(expression, first_number)

    if not next_expr:
        return float(first_number)
    operator = get_next_operator(expression, first_number)
    if operator == "+":
        return float(first_number) + calculate(next_expr)
    elif operator == "-":
        return float(first_number) - calculate(next_expr)
    elif operator == "*":
        return float(first_number) * calculate(next_expr)


def get_first_number(expression: str) -> str:
    return expression.split(" ")[0]

def get_next_expression(initial_expr: str, first_number: str) -> str:
    next_expr_start_index = len(first_number) + 3
    return initial_expr[next_expr_start_index:]

def get_next_operator(initial_expr: str, first_number: str) -> str:
    return initial_expr[len(first_number) + 1]

