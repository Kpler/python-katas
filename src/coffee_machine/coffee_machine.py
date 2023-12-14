from dataclasses import dataclass
from enum import Enum


class Beverage(Enum):
    TEA = "tea"
    COFFEE = "coffee"
    CHOCOLATE = "hot_chocolate"


EMPTY_ORDER = ""

BEVERAGE_MAP = {
    Beverage.TEA: "T",
    Beverage.COFFEE: "C",
    Beverage.CHOCOLATE: "H",
}


@dataclass
class CoffeeMachine:
    order_beverage: Beverage | None = None
    sugar_quantity: int | None = None

    def get_order(self) -> str:
        return f"{BEVERAGE_MAP.get(self.order_beverage, EMPTY_ORDER)}::"

    def send_order(self, beverage: str, sugar_quantity: int = 0) -> None:
        beverage = Beverage(beverage)
        self.order_beverage = beverage
        self.sugar_quantity = sugar_quantity
