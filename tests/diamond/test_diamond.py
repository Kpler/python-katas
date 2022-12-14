from src.diamond import get_diamond


def test_diamond_printer_a():
    result = get_diamond('A')
    assert result == 'A\n'


def test_diamond_printer_b():
    result = get_diamond('B')
    assert result == ' A \nB B\n A \n'


def test_diamond_printer_C():
    result = get_diamond('C')
    assert result == '  A  \n B B \nC   C\n B B \n  A  \n'
