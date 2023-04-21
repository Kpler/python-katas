def calculate(expression: str) -> float:
    expr_no_space = remove_spaces(expression)
    if not expr_no_space:
        return 0
    first_number, remainder_expr = get_first_number_and_expression(expr_no_space)
    return first_number + calculate(remainder_expr)


def remove_spaces(expression: str) -> str:
    return expression.replace(" ", "")

def get_first_number_and_expression(expression: str) -> float:
    operator = "+"
    split_values = expression.split(operator)
    return float(split_values[0]), "+".join(split_values[1:])

