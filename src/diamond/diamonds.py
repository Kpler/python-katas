import string

ALPHABET = list(string.ascii_uppercase)


def build_diamond(letter: str) -> str:
    iteration_count = get_iteration_count(letter)

    result = ""
    for i in range(iteration_count):
        number_of_spaces = iteration_count - 1
        row = ""
        result += row

    return letter


def get_iteration_count(letter: str) -> int:
    letter_index = ALPHABET.index(letter)
    iteration_count = letter_index + 1
    return iteration_count
