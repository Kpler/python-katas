import enum


class DrinkType(enum.Enum):
    COFFEE: str = "C"
    TEA: str = "T"
    HOT_CHOCOLATE: str = "H"

    def get_price(self) -> float:
        match self:
            case DrinkType.COFFEE:
                return 0.6
            case DrinkType.TEA:
                return 0.4
            case DrinkType.HOT_CHOCOLATE:
                return 0.5
            case _:
                raise ValueError("Can't resolve price from drink type")


def make_order(type: DrinkType, number_of_sugar: int) -> str:

    is_no_sugar = number_of_sugar < 1

    sugar_string, stick_string = ("", "") if is_no_sugar else (str(number_of_sugar), "0")

    return f"{type.value}:{sugar_string}:{stick_string}"


def create_order(
        drink_type: DrinkType,
        number_of_sugar: int,
        thune: float
) -> str:
    if thune < drink_type.get_price():
        return "M:not enough_cash"
    else:
        return make_order(drink_type, number_of_sugar)
