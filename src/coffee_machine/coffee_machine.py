from enum import Enum


class Drink(Enum):
    COFFEE = 0
    TEA = 1
    CHOCOLATE = 2

drink_map = {
    Drink.COFFEE: "C",
    Drink.TEA: "T",
    Drink.CHOCOLATE: "H",
}

class CoffeeMachineException(Exception):
    pass

class CoffeeMachine:

    def _check_funds(self):
        pass

    def _make_drink(self, drink: Drink, sugar: int) -> str:
        if not (drink_as_string := drink_map.get(drink)):
            raise CoffeeMachineException

        if sugar > 2:
            return "M:Don't take too much sugar. It's bad for your health!"

        (stick_as_string, sugar_as_string) = ("0", str(sugar)) if sugar >0 else ('', '')

        return f"{drink_as_string}:{sugar_as_string}:{stick_as_string}"

    def order_drink(self, drink: Drink, sugar: int, money: float) -> str:
        self._check_funds()
        return self._make_drink(drink, sugar)
