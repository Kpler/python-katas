import dataclasses
from enum import Enum


class Drink(Enum):
    TEA = 'tea'
    COFFEE = 'coffee'
    HOT_CHOCOLATE = 'hot chocolate'


@dataclasses.dataclass
class Order:
    drink: Drink
    sugars: int
    stick: bool


class CoffeeMachine:
    def process(self, order: str) -> str:
        return order

    def parser(self, order: str) -> Order:
        drink, sugars, _ = order.split(":")
        return Order(drink=drink, sugars=sugars, stick=False)
