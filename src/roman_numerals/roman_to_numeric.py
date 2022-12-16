from src.roman_numerals.roman_numerals import roman_numbers


def translate_roman_to_numeric(roman: str) -> int:
    count = 0
    remainder = roman

    while remainder != "":
        letter = remainder[:1]
        two_letters = remainder[:2]

        for item in roman_numbers:
            value = item["value"]
            symbol = item["symbol"]

            if two_letters == symbol:
                count += value
                remainder = remainder[2:]
                break

            if letter == symbol:
                count += value
                remainder = remainder[1:]
                break

    return count
