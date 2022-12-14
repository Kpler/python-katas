def make_diamond(diamond_letter):
    letter_int = ord(diamond_letter) - 65

    print(letter_int)

    lines_list = []
    for i in range(letter_int + 1):
        line = " " * (letter_int - i)
        line += chr(i + 65)
        line += " " * (i * 2 - 1)
        if i > 0:
            line += chr(i + 65)
        lines_list.append(line)

    return lines_list
