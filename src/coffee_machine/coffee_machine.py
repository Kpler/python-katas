
def make_order(type: str, number_of_sugar: int) -> str:

    is_no_sugar = number_of_sugar < 1

    sugar_string, stick_string = ("", "") if is_no_sugar else (str(number_of_sugar), "0")

    return f"{type}:{sugar_string}:{stick_string}"


class drink_type(enumerate):