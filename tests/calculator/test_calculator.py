from src.calculator.calculator import calculate


# def test_calculator_single_number_0():
#     assert calculate("0") == 0
#
#
# def test_calculator_single_number_1():
#     assert calculate("1") == 1
#
#
# def test_calculator_add():
#     assert calculate("1 + 1") == 2
#
# def test_calculator_sub():
#     assert calculate("3 - 2") == 1

def test_calculator_longer_add():
    # assert calculate("4 + 8 + 15 + 16 + 23 + 42") == 108
    assert calculate("100 - 50 + 25") == 75
    assert calculate("10 + 20 - 5") == 25
