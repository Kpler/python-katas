from src.roman_numerals.roman_to_numeric import translate_roman_to_numeric


def test_translate_I() -> None:
    assert translate_roman_to_numeric("I") == 1


def test_translate_V() -> None:
    assert translate_roman_to_numeric("V") == 5


def test_translate_LV() -> None:
    assert translate_roman_to_numeric("LV") == 55


def test_translate_IV() -> None:
    assert translate_roman_to_numeric("IV") == 4


def test_translate_XCIX() -> None:
    assert translate_roman_to_numeric("XCIX") == 99


def test_translate_CDL() -> None:
    assert translate_roman_to_numeric("CDL") == 450


def test_translate_CM() -> None:
    assert translate_roman_to_numeric("CM") == 900


def test_translate_2014() -> None:
    assert translate_roman_to_numeric("MMXIV") == 2014
