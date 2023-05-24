from src.calculator.calculator import calculate
import pytest


@pytest.mark.parametrize(
    "provided_string,expected_result",
     [
         ("1 + 1", 2),
         ("1 + 2", 3),
         ("5 - 2", 3),
         ("10 + 20 - 5", 25),
         ("100 - 50 + 25", 75),
         ("4 + 8 + 15 + 16 + 23 + 42", 108),
     ]
)
def test_calculator_add(provided_string: str, expected_result: float):
    assert calculate(provided_string) == expected_result


@pytest.mark.parametrize(
    "provided_string,expected_result",
     [
         ("2 * 3", 6),
         ("2 * 5 * 10", 100),
         ("2 + 3 * 4", 14),
     ]
)
def test_calculator_mult(provided_string: str, expected_result: float):
    assert calculate(provided_string) == expected_result
