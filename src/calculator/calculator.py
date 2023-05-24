from enum import Enum
from operator import add, sub


class Operators(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"

    def map_to_operator(self):
        match self:
            case Operators.ADD:
                return add
            case Operators.SUBTRACT:
                return sub


def calculate(expression: str) -> float:
    split_expression = expression.split(" ")

    unresolved_operators: list[Operators] = [Operators.ADD]

    result = 0
    for n in split_expression:
        if n in [o.value for o in Operators]:
            unresolved_operators.append(Operators(n))
        elif n.lstrip('-').isdigit():
            operation = unresolved_operators.pop()
            result = operation.map_to_operator()(result, float(n))

    return result
