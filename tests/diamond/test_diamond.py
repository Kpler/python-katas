from src.diamond import get_diamond


def test_diamond_printer_a():
    result = get_diamond('A')
    assert result == 'A'


def test_diamond_printer_b():
    result = get_diamond('B')
    assert result == ' A \nB B\n A '
