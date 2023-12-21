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

BEVERAGE_PRICES = {
    Beverage.TEA: 0.4,
    Beverage.COFFEE: 0.6,
    Beverage.HOT_CHOCOLATE: 0.5,
}

class DrinkMaker:
    def make(self, order: Beverage | str, sugar: int = 0, amount: float = 10) -> str:
        sugar_output = ":" if sugar == 0 else f"{sugar}:0"
        beverage_output = BEVERAGE_TO_COMMAND.get(order)
        cost = BEVERAGE_PRICES.get(order)

        if beverage_output is not None and cost is not None:
            if amount < cost:
                return f"M:Missing {round((cost - amount),1)}"
            return f"{beverage_output}:{sugar_output}"
        else:
            return f"M:{order}"
