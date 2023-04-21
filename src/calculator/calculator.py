from operator import add, mul, sub
import re

operations = {
    "+": add,
    "-": sub,
    "*": mul,
}


def calculate(expression: str) -> int:
    tokens = expression.split()
    head = tokens[0]

    foo(tokens)

    return rec(int(head), tokens[1:])


def foo(tokens: list[str]) -> None:
    if (len(tokens) % 2) == 0:
        raise ValueError("No enough element")

    branches = re.split(r"[\s+-\*\/]", " ".join(tokens))
    for branch in branches:
        if len(branch) == 1:
            yield branch
        else:
            head = branch.split()[0]
            yield rec(int(head), branch.split()[1:])


def rec(acc: int, tokens: list[str]) -> int:
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
