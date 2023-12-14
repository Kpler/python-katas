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
        if not self.order_beverage:
            return EMPTY_ORDER
        return f"{self._translate_order_beverage()}:{self._translate_order_sugar_quantity()}:{self._translate_order_stick()}"

    def _translate_order_beverage(self):
        return BEVERAGE_MAP[self.order_beverage]
    
    def _translate_order_sugar_quantity(self):
        if self._is_there_sugar():
            return self.sugar_quantity
        return ''
    
    def _translate_order_stick(self):
        if self._is_there_sugar():
            return '0'
        return ''
    
    def _is_there_sugar(self) -> bool:
        return self.sugar_quantity > 0

    def send_order(self, beverage: str, sugar_quantity: int = 0) -> None:
        beverage = Beverage(beverage)
        self.order_beverage = beverage
        self.sugar_quantity = sugar_quantity
