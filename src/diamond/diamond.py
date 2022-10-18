ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def create_diamond(letter: str) -> str:
    if len(letter) != 1:
        raise ValueError

    character_place = ALPHABET.index(letter.upper())
    line_width = character_place * 2 + 1

    lines = []
    for i in range(-character_place, character_place + 1):
        current_char_index = character_place - abs(i)
        current_char = ALPHABET[current_char_index]
        is_letter_a = current_char_index == 0

        outer_gap = abs(i)
        inner_gap = line_width - outer_gap * 2 - (1 if is_letter_a else 2)

        optional_char = current_char if not is_letter_a else ""
        outer_spaces = " " * outer_gap
        inner_spaces = " " * inner_gap
        output_line = (
            f"{outer_spaces}{current_char}{inner_spaces}{optional_char}{outer_spaces}"
        )
        lines.append(output_line)

    return "\n".join(lines)
