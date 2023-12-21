from enum import Enum, auto
from typing import Literal


class DrinkType(Enum):
    Tea = auto()
    Coffee = auto()
    Chocolate = auto()
    OrangeJuice = auto()


class CoffeeMaker:
    prices = {
        DrinkType.Tea: 0.4,
        DrinkType.Coffee: 0.6,
        DrinkType.Chocolate: 0.5,
        DrinkType.OrangeJuice: 0.6,
    }
    codes = {
        DrinkType.Tea: "T",
        DrinkType.Coffee: "C",
        DrinkType.Chocolate: "H",
        DrinkType.OrangeJuice: "O",
    }
    drink_sold = {
        DrinkType.Tea: 0,
        DrinkType.Coffee: 0,
        DrinkType.Chocolate: 0,
        DrinkType.OrangeJuice: 0,
    }
    money = 0

    def _get_money_difference(self, drink_type: DrinkType, money: float) -> float:
        return money - self.prices[drink_type]
    
    def make_drink(self, drink_type: DrinkType, money: float, nb_of_sugar: Literal[0, 1, 2] = 0, extra_hot: bool = False) -> str:

        diff = self._get_money_difference(drink_type, money)
        if diff < 0:
            return f"M:you-miss-{round(abs(diff), 2)}-EURO-to-make-a-drink"

        if nb_of_sugar > 2:
            return "M:sugar-is-not-good-for-your-health"
        if nb_of_sugar > 0 and drink_type == DrinkType.OrangeJuice:
            return "M:do-not-put-sugar-in-your-orange-juice"
        if extra_hot and drink_type == DrinkType.OrangeJuice:
            return "M:do-not-make-hot-orange-juice"

        self.money += money
        self.drink_sold[drink_type] += 1

        _drink = f"{self.codes[drink_type]}{'h' if extra_hot else ''}"
        _sugar = str(nb_of_sugar) if nb_of_sugar else ""

        _stick = "0" if _sugar else ""
        return f"{_drink}:{_sugar}:{_stick}"

    def get_report(self):
        return self.drink_sold | {"money": self.money}
