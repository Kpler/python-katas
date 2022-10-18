import pytest
from src.diamond.diamond import create_diamond


def test_input_a() -> None:
    assert create_diamond("a") == "A"


def test_input_garbage() -> None:
    with pytest.raises(ValueError):
        create_diamond("garbage")
    with pytest.raises(ValueError):
        create_diamond("1")
    with pytest.raises(ValueError):
        create_diamond("%")
    with pytest.raises(ValueError):
        create_diamond("")
    with pytest.raises(ValueError):
        create_diamond("abcd")


def test_input_b() -> None:
    assert create_diamond("b") == " A \nB B\n A "


def test_input_c() -> None:
    assert create_diamond("c") == "  A  \n B B \nC   C\n B B \n  A  "
