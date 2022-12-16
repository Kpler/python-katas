from src.roman_numerals import translate_numeric_to_roman


def test_translate_1() -> None:
    assert translate_numeric_to_roman(1) == "I"


def test_translate_5() -> None:
    assert translate_numeric_to_roman(5) == "V"


def test_translate_55() -> None:
    assert translate_numeric_to_roman(55) == "LV"
