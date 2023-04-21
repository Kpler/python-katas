from src.calculator.calculator import calculate


def test_calculator_add():
    assert calculate("1 + 1") == 2
    assert calculate("1 + 1 + 1") == 3
    assert calculate("2 + 1") == 3

def test_calculator_substraction():
    assert calculate("1 - 1") == 0