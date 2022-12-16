from typing import TypedDict


class RomanNumber(TypedDict):
    value: int
    symbol: str


roman_numbers: list[RomanNumber] = [
    {"value": 1, "symbol": "I"},
    {"value": 5, "symbol": "V"},
    {"value": 10, "symbol": "X"},
    {"value": 50, "symbol": "L"},
    {"value": 100, "symbol": "C"},
    {"value": 500, "symbol": "D"},
    {"value": 1000, "symbol": "M"},
]


def translate_numeric_to_roman(numeric: int) -> str:
    output = ""
    remainder = numeric
    for item in reversed(roman_numbers):
        value = item["value"]
        symbol = item["symbol"]
        while remainder / value >= 1:
            output += symbol
            remainder -= value

    return output
