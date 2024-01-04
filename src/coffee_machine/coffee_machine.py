from enum import Enum, auto


class Drink(Enum):
    COFFEE = auto()
    TEA = auto()
    CHOCOLATE = auto()
    ORANGE_JUICE = auto()

drink_type_to_letter = {
    Drink.COFFEE: "C",
    Drink.CHOCOLATE: "H",
    Drink.TEA: "T",
    Drink.ORANGE_JUICE: "O",
}

drink_price = {
    Drink.COFFEE: 0.6,
    Drink.CHOCOLATE: 0.5,
    Drink.TEA: 0.4,
    Drink.ORANGE_JUICE: 0.6,
}

class DrinkMaker:
    def _check_orange_juice_inputs(self, sugar: int, is_extra_hot: bool) -> str | None:
        if sugar > 0:
            return "M:no sugar in orange juice"
        if is_extra_hot:
            return "M:are you out of your mind"
        return None

    def make_drink(self, drink_type: Drink, sugar: int, money: float, is_extra_hot: bool) -> str:
        if drink_type == Drink.ORANGE_JUICE and (error := self._check_orange_juice_inputs(sugar, is_extra_hot)) is not None:
            return error

        if sugar > 2:
            return "M:no diabete"

        money_difference = drink_price[drink_type] - money
        if money_difference > 0:
            return f"M:missing {money_difference}"

        drink_type_code = drink_type_to_letter[drink_type]
        is_extra_hot_code = "h" if is_extra_hot else ""
        sugar_code, stick = (str(sugar), "0") if sugar != 0 else ("", "")
        return f'{drink_type_code}{is_extra_hot_code}:{sugar_code}:{stick}'
