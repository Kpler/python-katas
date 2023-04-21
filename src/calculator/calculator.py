from typing import Tuple
from enum import Enum   

Operator = Enum('Operator', ['+','-','*','/'])

def calculate(expression: str) -> float:
    operator = find_operator(expression)
    return sum(find_operands(expression, operator))

def find_operands(string:str, operator: Operator) -> list[int,int]:
    return list(map(int, string.split(operator.value)))

def find_operator(string: str) -> Operator:
    for operator in Operator:
        if operator.value in string:
            return operator