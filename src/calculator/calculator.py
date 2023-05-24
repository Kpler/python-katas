operators: list[str] = ["+", "-"]

def calculate(expression: str) -> float:
    split_expression = expression.split(" ")

    unresolved_opertors: list[Operators]= []
    sum = 0
    for n in split_expression:
        if n in operators:
            unresolved_opertors += n
        elif n.isdigit():
            sum += float(n)
    return sum
