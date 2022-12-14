from src.diamond import get_diamond_string


def test_diamond_printer_a():
    result = get_diamond_string("A")
    assert result == "A\n"


def test_diamond_printer_b():
    result = get_diamond_string("B")
    assert result == " A \nB B\n A \n"


def test_diamond_printer_c():
    result = get_diamond_string("C")
    assert result == "  A  \n B B \nC   C\n B B \n  A  \n"
