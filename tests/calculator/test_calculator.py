from src.calculator.calculator import calculate


def test_calculator_add():
    assert calculate("1 + 1") == 2

def test_calculator_addition_multiple():
    assert calculate("1 + 2 + 3") == 6
