from typing import Tuple, List
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

def find_operands(string:str, operator: Operator) -> List[int,int]:
    return list(map(int, string.split(operator.name)))

def find_operators(string: str) -> List[Operator]:
    result = re.sub(r'[0-9]+', '', string) # "-+"
    #return list(filter(lambda x: x in Operator.value, string.split(" ")))
    #for operator in Operator:
    #    if operator.value in string:
    #        return operator


