def calculate(expression: str) -> float:
    expr_no_space = remove_spaces(expression)
    if not expr_no_space:
        return 0
    first_number = get_first_number(expr_no_space)
    next_expr_start_index = len(first_number) + 1
    next_expr = expr_no_space[next_expr_start_index:]
    return float(first_number) + calculate(next_expr)


def remove_spaces(expression: str) -> str:
    return expression.replace(" ", "")


def get_first_number(expression: str) -> str:
    operator = "+"
    return expression.split(operator)[0]

