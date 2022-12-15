A_ASCII_NUMBER = 65
Z_ASCII_NUMBER = 90


def print_diamond(input: str) -> None:
    letter_ascii_number = ord(input)
    number_of_spaces = letter_ascii_number - A_ASCII_NUMBER
    print(build_diamond(input))

def build_diamond(input: str, number_of_spaces: int = 0) -> str:
    letter_ascii_number = ord(input)
    distance_to_a = letter_ascii_number - A_ASCII_NUMBER
    if distance_to_a == 0:
        return " " + input + " "
    return build_diamond(chr(letter_ascii_number - 1), distance_to_a) + '' + build_diamond(chr(letter_ascii_number - 1), distance_to_a)

''''
  A
 B B
C   C
 B B
  A
'''