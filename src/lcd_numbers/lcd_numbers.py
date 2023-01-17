ONE = """
   
  |
  |
"""

TWO = """
 _ 
 _|
|_ 
"""

THREE = """
 _ 
 _|
 _|
"""

FOUR = """
   
|_|
  |
"""

FIVE = """
 _ 
|_
 _|
"""

SIX = """
 _ 
|_ 
|_|
"""

SEVEN = """
 _ 
  |
  |
"""

EIGHT = """
 _ 
|_|
|_|
"""

NINE = """
 _ 
|_|
 _|
"""

LCD_DIGITS = {
    "1": ONE,
    "2": TWO,
    "3": THREE,
    "4": FOUR,
    "5": FIVE,
    "6": SIX,
    "7": SEVEN,
    "8": EIGHT,
    "9": NINE,
}


def _get_lcd_digit(digit: str) -> str:
    return LCD_DIGITS[digit][1:-1]


def display_lcd(number: int) -> str:
    output_rows = ["", "", ""]

    for digit in str(number):
        lcd_digit = _get_lcd_digit(digit)
        digit_rows = lcd_digit.split("\n")

        for index, row in enumerate(digit_rows):
            output_rows[index] += row

    return "\n".join(output_rows)
