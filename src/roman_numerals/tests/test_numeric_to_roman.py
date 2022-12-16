from src.roman_numerals.numeric_to_roman import translate_numeric_to_roman


def test_translate_1() -> None:
    assert translate_numeric_to_roman(1) == "I"


def test_translate_5() -> None:
    assert translate_numeric_to_roman(5) == "V"


def test_translate_55() -> None:
    assert translate_numeric_to_roman(55) == "LV"


def test_translate_4() -> None:
    assert translate_numeric_to_roman(4) == "IV"


def test_translate_99() -> None:
    assert translate_numeric_to_roman(99) == "XCIX"


def test_translate_450() -> None:
    assert translate_numeric_to_roman(450) == "CDL"


def test_translate_900() -> None:
    assert translate_numeric_to_roman(900) == "CM"


def test_translate_2014() -> None:
    assert translate_numeric_to_roman(2014) == "MMXIV"
