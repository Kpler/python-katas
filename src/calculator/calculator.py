from operator import add, sub


def calculate(expression: str) -> float:
    tokens = expression.split()

    return rec(tokens)


def rec(tokens):
    if len(tokens) == 0:
        return 0
    elif len(tokens) == 1:
        return int(tokens[0])
    else:
        head = tokens[0]
        op = tokens[1]

        if op == "+":
            f = add
        elif op == "-":
            f = sub
        else:
            raise ValueError(f"Unexpected Operation {op}")
        try:
            a = int(head)

        except:
            raise

        return f(a, rec(tokens[2:]))
