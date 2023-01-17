from src.lcd_numbers.lcd_numbers import display_lcd


def test_1() -> None:
    expected = """
   
  |
  |
"""
    assert display_lcd(1) == expected[1:-1]


def test_2() -> None:
    expected = """
 _ 
 _|
|_ 
"""
    assert display_lcd(2) == expected[1:-1]


def test_12() -> None:
    expected = """
    _ 
  | _|
  ||_ 
"""
    assert display_lcd(12) == expected[1:-1]
