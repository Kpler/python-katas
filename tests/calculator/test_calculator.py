from src.calculator.calculator import calculate


def test_calculator_add():
    assert calculate("1 + 1") == 2
