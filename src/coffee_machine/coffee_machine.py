
def make_order(type: str, number_of_sugar: int) -> str:

    sugar_string = "" if number_of_sugar < 1 else str(number_of_sugar)
    stick_string = "0" if  number_of_sugar >= 1 else ""

    return f"{type}:{sugar_string}:{stick_string}"
