alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


LINE_SEPARATOR = "\n"
SPACE = " "
EMPTY_STRING = ""


Diamond = list[str]


def get_top_rows(letter: str) -> Diamond:
    top_rows: Diamond = []

    input_letter_index = alphabet.index(letter)
    row_length = input_letter_index * 2 + 1

    for i in range(input_letter_index + 1):
        letter_this_row = alphabet[i]
        number_of_spaces_edge = input_letter_index - i
        number_of_spaces_in_the_middle = row_length - 2 - number_of_spaces_edge * 2

        has_middle_spaces = number_of_spaces_in_the_middle > 0
        second_letter = letter_this_row if has_middle_spaces else EMPTY_STRING

        row = (
            SPACE * number_of_spaces_edge
            + letter_this_row
            + SPACE * number_of_spaces_in_the_middle
            + second_letter
            + SPACE * number_of_spaces_edge
        )

        top_rows.append(row)

    return top_rows


def get_rows(letter: str) -> Diamond:
    top_rows = get_top_rows(letter)
    bottom_rows = list(reversed(top_rows[:-1]))
    all_rows = top_rows + bottom_rows
    return all_rows


def diamond_to_string(diamond: Diamond) -> str:
    return LINE_SEPARATOR.join(diamond) + LINE_SEPARATOR


def get_diamond(letter: str) -> str:
    diamond = get_rows(letter)
    output_string = diamond_to_string(diamond)
    return output_string
