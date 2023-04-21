from src.calculator.calculator import calculate, find_operators


def test_calculator_add():
    assert calculate("1 + 1") == 2
    assert calculate("1 + 1 + 1") == 3
    assert calculate("2 + 1") == 3

def test_calculator_substraction():
    assert calculate("1 - 1") == 0

def test_find_operators():
    assert find_operators("1 - 1 + 3") == ["-", "+"]