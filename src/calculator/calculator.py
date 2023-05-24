from enum import Enum
from operator import add, subtract
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
                return subtract

def calculate(expression: str) -> float:
    split_expression = expression.split(" ")

    unresolved_opertors: list[Operators]= []

    sum = 0
    for n in split_expression:
        if n in [o.value for o in Operators]:
            unresolved_opertors += n
        elif n.isdigit():
            sum += float(n)
        print(unresolved_opertors)
    return sum
