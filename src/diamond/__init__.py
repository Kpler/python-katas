alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


LINE_SEPARATOR = "\n"
SPACE = " "


def get_diamond(letter: str) -> str:
    input_letter_index = alphabet.index(letter)

    size = input_letter_index * 2 + 1
    rows = []
    for i in range(input_letter_index + 1):
        letter_this_row = alphabet[i]
        number_of_spaces_edge = input_letter_index - i
        number_of_spaces_in_the_middle = size - 2 - number_of_spaces_edge * 2

        if i == 0:
            row = (
                SPACE * number_of_spaces_edge
                + letter_this_row
                + SPACE * number_of_spaces_edge
            )
        else:
            row = (
                SPACE * number_of_spaces_edge
                + letter_this_row
                + SPACE * number_of_spaces_in_the_middle
                + letter_this_row
                + SPACE * number_of_spaces_edge
            )

        rows.append(row)

    rows = rows + list(reversed(rows[:-1]))

    return LINE_SEPARATOR.join(rows) + LINE_SEPARATOR
