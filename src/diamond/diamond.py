A_ASCII_NUMBER = 65
Z_ASCII_NUMBER = 90


def print_diamond(input: str) -> None:
    letter_ascii_number = ord(input)
    number_of_spaces = letter_ascii_number - A_ASCII_NUMBER
    print(build_diamond(input))

def build_diamond(input: str) -> str:
    return input

''''
  A
 B B
C   C
 B B
  A
'''