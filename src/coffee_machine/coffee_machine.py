from dataclasses import dataclass
from enum import Enum


class Beverage(Enum):
    TEA  = "tea"
    COFFEE = "coffee"
    CHOCOLATE = "hot_chocolate"

EMPTY_ORDER = ""

BEVERAGE_MAP = {
    Beverage.TEA: "T::",
    Beverage.COFFEE: "C::",
    Beverage.CHOCOLATE: "H::",
}

@dataclass
class CoffeeMachine:
    order_beverage: Beverage | None = None

    def get_order(self) -> str:
        return BEVERAGE_MAP.get(self.order_beverage, EMPTY_ORDER)

    def send_order(self, beverage: str) -> None:
        beverage = Beverage(beverage)
        self.order_beverage = beverage
