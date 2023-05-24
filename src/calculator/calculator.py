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

    unresolved_opertors: list[Operators]= [Operators.ADD]

    sum = 0
    for n in split_expression:
        if n in [o.value for o in Operators]:
            unresolved_opertors.append(Operators(n))
        elif n.isdigit():
            operation = unresolved_opertors.pop()
            sum = operation.map_to_operator()(sum, float(n))

        print(unresolved_opertors)
    return sum
