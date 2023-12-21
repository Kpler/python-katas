from enum import Enum


class Beverage(Enum):
    TEA = "Tea"
    COFFEE = "Coffee"
    HOT_CHOCOLATE = "Hot Chocolate"


BEVERAGE_TO_COMMAND = {
    Beverage.TEA: "T",
    Beverage.COFFEE: "C",
    Beverage.HOT_CHOCOLATE: "H",
}

class DrinkMaker:
    def make(self, order: Beverage | str, sugar: int = 0, amount: float = 10) -> str:
        sugar_output = ":" if sugar == 0 else f"{sugar}:0"
        beverage_output = BEVERAGE_TO_COMMAND.get(order)

        if beverage_output is not None:
            if amount == 0:
                return "M:Missing 0.4"
            return f"{beverage_output}:{sugar_output}"
        else:
            return f"M:{order}"
