def calculate(expression: str) -> float:
    if not expression:
        return 0

    expr_without_multiplication = expression
    if "*" in expr_without_multiplication:
        expr_without_multiplication = manage_multiplication(expression)

    return manage_addition_substraction(expr_without_multiplication)


def manage_multiplication(expression: str):
    split_expr = expression.split(" ")
    expr_without_multiplication = []
    for i in range(len(split_expr)):
        if split_expr[i] == "*":
            expr_without_multiplication[-1] = str(float(expr_without_multiplication[-1]) * float(split_expr[i + 1]))
        elif split_expr[i - 1] == "*":
            pass
        else:
            expr_without_multiplication.append(split_expr[i])

    return " ".join(expr_without_multiplication)


def manage_addition_substraction(expression: str) -> float:
    first_number = get_first_number(expression)
    next_expr = get_next_expression(expression, first_number)
    if not next_expr:
        return float(first_number)
    operator = get_next_operator(expression, first_number)
    if operator == "+":
        return float(first_number) + calculate(next_expr)
    elif operator == "-":
        return float(first_number) - calculate(make_opposite(next_expr))


def get_first_number(expression: str) -> str:
    return expression.split(" ")[0]


def get_next_expression(initial_expr: str, first_number: str) -> str:
    next_expr_start_index = len(first_number) + 3
    return initial_expr[next_expr_start_index:]


def get_next_operator(initial_expr: str, first_number: str) -> str:
    return initial_expr[len(first_number) + 1]


def make_opposite(expression: str) -> str:
    split_expr = expression.split(" ")
    opposite_expr = []
    for value in split_expr:
        if value == "+":
            opposite_expr.append("-")
        elif value == "-":
            opposite_expr.append("+")
        else:
            opposite_expr.append(value)
    return " ".join(opposite_expr)
