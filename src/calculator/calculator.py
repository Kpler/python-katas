from typing import Tuple
from enum import Enum   
import re

class Operator(Enum):
    ADD = "+"
    SUBSTRACT = "-"
    MULTIPLY = "*"
    DIVISION = "/"


def calculate(expression: str) -> float:
    operator = find_operators(expression)
    if operator == Operator.ADD:
        return sum(find_operands(expression, operator))
    else:
        return find_operands(expression, operator)[0] - find_operands(expression, operator)[1]

def find_operands(string:str, operator: Operator) -> list[int,int]:
    return list(map(int, string.split(operator.name)))

def find_operators(string: str) -> list[Operator]:
    result = list(re.sub(r'[0-9]+',"", string).replace(" ", ""))
    print(result)
    return result
    # return list(filter(lambda x: x in Operator.name, string.split(" ")))
    #for operator in Operator:
    #    if operator.value in string:
    #        return operator


