from src.calculator.calculator import calculate


def test_calculator_with_empty_expression():
    assert calculate("") == 0


def test_calculator_with_one_expression():
    assert calculate("1") == 1


def test_calculator_with_one_negative_expression():
    assert calculate("-1") == -1


def test_calculator_add():
    assert calculate("1 + 1") == 2


def test_calculator_add_equals_3():
    assert calculate("1 + 2") == 3


def test_addition_3_elements():
    assert calculate("1 + 1 + 1") == 3


def test_complex_addition_3_elements():
    assert calculate("10 + 20 + 5") == 35


def test_substract():
    assert calculate("2 - 1") == 1


def test_substract_equals_1():
    assert calculate("2 + -1") == 1


def test_addition_then_substraction():
    assert calculate("2 + 1 - 5") == -2


def test_substraction_then_addition():
    assert calculate("2 - 5 + 1") == -2


def test_substraction_then_addition_negative():
    assert calculate("2 - -5 + -1") == 6


def test_substract_negative_number():
    assert calculate("2 - -1") == 3


def test_readme_level_1():
    assert calculate("1 + 2") == 3
    assert calculate("5 - 3") == 2
    assert calculate("10 + 20 - 5") == 25
    assert calculate("100 - 50 + 25") == 75
    assert calculate("4 + 8 + 15 + 16 + 23 + 42") == 108


def test_multiplication():
    assert calculate("2 * 5") == 10


def test_multiplication_negative():
    assert calculate("2 * -5") == -10


def test_mulitple_multiplication():
    assert calculate("-2 * -5 * 3") == 30


def test_addition_then_multiplication_then_addition():
    assert calculate("3 + 2 * 5") == 13


def test_multiplication_then_addition():
    assert calculate("2 * 5 + 3") == 13


def test_readme_level_2():
    assert calculate("2 * 3") == 6
    assert calculate("2 * 5 * 10") == 100
    assert calculate("2 + 3 * 4") == 14
    assert calculate("2 * 3 + 4") == 10
    assert calculate("3 * 4 + 5 * 6") == 42