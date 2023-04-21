import pytest

from src.calculator.calculator import calculate


def test_calculator_single_number_0():
    assert calculate("0") == 0


def test_calculator_single_number_1():
    assert calculate("1") == 1


def test_calculator_add():
    assert calculate("1 + 1") == 2


def test_calculator_sub():
    assert calculate("3 - 2") == 1


def test_calculator_longer_add():
    assert calculate("4 + 8 + 15 + 16 + 23 + 42") == 108
    assert calculate("100 - 50 + 25") == 75
    assert calculate("10 + 20 - 5") == 25


def test_():
    with pytest.raises(ValueError):
        calculate("4 +")


def test_multiplication_simple():
    assert calculate("0 * 0") == 0
    assert calculate("0 * 1") == 0
    assert calculate("1 * 1") == 1
    assert calculate("1 * 2") == 2
    assert calculate("3 * 4") == 12

def test_multiplication_only():
    assert calculate("0 * 0 * 0") == 0
    assert calculate("0 * 1 * 5") == 0
    assert calculate("1 * 1 * 12") == 12
    assert calculate("1 * 2 * 6") == 12
    assert calculate("3 * 4 * 5") == 60

def test_multiplication_combined():
    assert calculate("2 + 3 * 4") == 14
    assert calculate("2 * 3 + 4") == 10
    assert calculate("3 * 4 + 5 * 6") == 42
