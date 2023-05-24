from src.calculator.calculator import calculate
import pytest


@pytest.mark.parametrize(
    "provided_string,expected_result",
     [
         ("1 + 1", 2),
         ("1 + 2", 3),
     ]
)
def test_calculator_add(provided_string: str, expected_result: float):
    assert calculate(provided_string) == expected_result


# 1 + 2 # Result: 3
# 5 - 3 # Result: 2
# 10 + 20 - 5 # Result: 25
# 100 - 50 + 25 # Result: 75
# 4 + 8 + 15 + 16 + 23 + 42 # Result: 108