import dataclasses
from enum import Enum

class DrinkType(Enum):
    COFFEE = 'C'
    TEA = 'T'
    HOT_CHOCOLATE = 'H'

    def price(self) -> float:
        if self.COFFEE:
            return 0.5
        elif self.TEA:
            return 0.4
        else:
            return 0.6

@dataclasses.dataclass
class Order:
    drink_type: DrinkType
    money: float = 0.0
    sugars: int = 0


class CoffeeMachine:
    def generate_order(self, order: Order) -> str:
        sugars_str = "" if order.sugars == 0 else order.sugars.__str__()
        stick = "" if order.sugars == 0 else "0"
        if order.money < order.drink_type.price():
            return "M:message-content"

        return f"{order.drink_type.value}:{sugars_str}:{stick}"
