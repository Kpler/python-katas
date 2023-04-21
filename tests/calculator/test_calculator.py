from src.calculator.calculator import calculate


def test_calculator_add():
    assert calculate("1 + 1") == 2


def test_calculator_add_equals_3():
    assert calculate("1 + 2") == 3


def test_calculator_with_empty_expression():
    assert calculate("") == 0


def test_calculator_with_one_expression():
    assert calculate("1") == 1


def test_addition_3_elements():
    assert calculate("1 + 1 + 1") == 3


def test_complex_addition_3_elements():
    assert calculate("10 + 20 + 5") == 35
