alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_diamond(letter: str) -> str:
    input_letter_index = alphabet.index(letter)

    size = input_letter_index * 2 + 1
    rows = ""
    for i in range(size):
        number_of_spaces = input_letter_index - 1 - i
        rows += " " * number_of_spaces + alphabet[i] + " " * number_of_spaces + "\n"

        # rows += " " * size + "\n"

    return rows
