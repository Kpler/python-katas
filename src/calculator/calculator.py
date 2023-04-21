def calculate(expression: str) -> float:
    tokens = expression.split()

    return rec(tokens)

def rec(tokens):
    if len(tokens) == 0:
        return 0
    else:
        head = tokens[0]
        op = tokens[1]

        if op == "+":
            f = lambda x, y: x + y
        elif op == "-":
            f = lambda x, y: x - y
        else:
            raise ValueError(f"Unexpected Operation {op}")
        try:
            a = int(head)

        except:
            raise

        return a + rec(tokens[1:])
