from dataclasses import dataclass
from enum import Enum

EMPTY_ORDER = ""
TEA_ORDER = "T::"
COFFEE_ORDER = "C::"
CHOCOLATE_ORDER = "H::"

class Beverage(Enum):
    TEA  = "tea"
    COFFEE = "coffee"
    CHOCOLATE = "hot_chocolate"

@dataclass
class CoffeeMachine:
    order_beverage: Beverage = None

    def get_order(self) -> str:
        if self.order_beverage == 'tea':
            return TEA_ORDER
        if self.order_beverage == 'coffee':
            return COFFEE_ORDER
        if self.order_beverage == 'hot_chocolate':
            return CHOCOLATE_ORDER
        return EMPTY_ORDER

    def send_order(self, beverage: str) -> None:
        beverage = Beverage(beverage)
        self.order_beverage = beverage
