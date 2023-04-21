from operator import add, sub


def calculate(expression: str) -> float:
    tokens = expression.split()
    head = tokens[0]

    return rec(int(head), tokens)


def rec(acc: int, tokens: list[str]) -> float:
    if len(tokens) == 0:
        return 0
    elif len(tokens) == 1:
        return int(tokens[0])
    else:
        op = tokens[0]
        head = tokens[1]

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
