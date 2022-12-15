A_ASCII_NUMBER = 65
Z_ASCII_NUMBER = 90


def print_diamond(input: str) -> None:
    letter_ascii_number = ord(input)
    number_of_spaces = letter_ascii_number - A_ASCII_NUMBER
    print(build_diamond(input))

def build_diamond(input: str, number_of_spaces: int = 0) -> str:
    letter_ascii_number = ord(input)
    distance_to_a = letter_ascii_number - A_ASCII_NUMBER

    spaces_before_and_after = ""
    for _ in range(number_of_spaces):
        spaces_before_and_after += " "

    if distance_to_a == 0:
        current_line = spaces_before_and_after + input + spaces_before_and_after
        return current_line

    spaces_between = ""
    for _ in range(distance_to_a):
        spaces_between += " "

    current_line = spaces_before_and_after + input + spaces_between + input + spaces_before_and_after

    previous_and_next_lines = build_diamond(chr(letter_ascii_number - 1), number_of_spaces + 1)

    return previous_and_next_lines + '\n' + current_line + '\n' + previous_and_next_lines

'''
  A
 B B
C   C
 B B
  A
'''