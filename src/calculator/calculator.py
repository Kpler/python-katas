from operator import add, sub


operations = {
 "+": add,
 "-": sub,
}

def calculate(expression: str) -> float:
    tokens = expression.split()
    head = tokens[0]

    if (len(tokens) % 2) == 0:
        raise ValueError("No enough element")

    return rec(int(head), tokens[1:])


def rec(acc: int, tokens: list[str]) -> float:
    if len(tokens) == 0:
        return acc
    else:
        op = tokens[0]
        head = tokens[1]

        try:
            operation = operations[op]
        except:
            raise ValueError(f"Unexpected Operation {op}")
       
        try:
            a = int(head)

        except:
            raise

        return rec(operation(acc, a), tokens[2:])
