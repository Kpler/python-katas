import enum

class DrinkType(enum.Enum):
    COFFEE: str = "C"
    TEA: str = "T"
    HOT_CHOCOLATE: str = "H"


def make_order(type: DrinkType, number_of_sugar: int) -> str:

    is_no_sugar = number_of_sugar < 1

    sugar_string, stick_string = ("", "") if is_no_sugar else (str(number_of_sugar), "0")

    return f"{type.value}:{sugar_string}:{stick_string}"


def create_order(drink_type: DrinkType, number_of_sugar: int,
                 thune: float) -> str:
    if thune==0:
        return "M:not enough_cash"