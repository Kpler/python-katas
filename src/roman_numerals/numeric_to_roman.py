from src.roman_numerals.roman_numerals import roman_numbers


def translate_numeric_to_roman(numeric: int) -> str:
    output = ""
    remainder = numeric
    for index, item in enumerate(roman_numbers):
        value = item["value"]
        symbol = item["symbol"]
        while remainder / value >= 1:
            output += symbol
            remainder -= value

    return output
