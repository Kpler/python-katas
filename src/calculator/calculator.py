from typing import Tuple
from enum import Enum   

Operator = Enum('Operator', ['+','-','*','/'])
# operator = ["+", "-"]

def calculate(expression: str) -> float:
    operator = find_operator(expression)
    if operator.name == "+":
        return sum(find_operands(expression, operator))
    else:
        return find_operands(expression, operator)[0] - find_operands(expression, operator)[1]

def find_operands(string:str, operator: Operator) -> list[int,int]:
    return list(map(int, string.split(operator.name)))

def find_operator(string: str) -> Operator:
    for operator in Operator:
        if operator.name in string:
            return operator


