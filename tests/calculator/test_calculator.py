import pytest

from src.calculator.calculator import calculate


@pytest.mark.parametrize(
    "input, expected_result",
    [
        ("1 + 1", 2),
        ("1 + 2 + 3", 6),
        ("1 - 1", 0),
        ("10 + 20 - 5", 25),
        ("10 + -20", -10),
        ("+ 1 + 1", 2),
        ("- 1 + 1", 0),
        ("1 + 2 + 3 +", 6),
        # ("10 10", -10),
        # ("hellooooo", -10),
    ]
)
def test_calculator(input: str, expected_result: float):
    assert calculate(input) == expected_result
