from typing import Tuple


def calculate(expression: str) -> float:
    return sum(find_operands(expression))

def find_operands(string: str) -> Tuple[int,int]:
    return list(map(int, string.split("+")))

def find_operator(string: str) -> str:
    pass