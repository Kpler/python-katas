from src.diamond.diamonds import build_diamond
import pytest

@pytest.mark.parametrize(
    "letter",
    [
        "A",
        "B"
    ]
)
def test_build_diamond_return_given_letter(letter):
    assert build_diamond(letter) == letter