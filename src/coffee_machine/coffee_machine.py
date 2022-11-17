import dataclasses
from enum import Enum

class DrinkType(Enum):
    COFFEE = 'C'
    TEA = 'T'
    HOT_CHOCOLATE = 'H'

@dataclasses.dataclass
class Order:
    drink_type: DrinkType
    sugars: int = 0


class CoffeeMachine:
    def generate_order(self, order: Order) -> str:
        sugars_str = "" if order.sugars == 0 else order.sugars.__str__()
        stick = "" if order.sugars == 0 else "0"
        return f"{order.drink_type.value}:{sugars_str}:{stick}"
