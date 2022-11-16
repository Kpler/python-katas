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

    DRINK_MATCHING = {
        'T': Drink.TEA,
        'C': Drink.COFFEE,
        'H': Drink.HOT_CHOCOLATE,
    }

    def process(self, order: str) -> str:
        return self.parser(order)

    def parser(self, order: str) -> Order:
        drink, sugars, _ = order.split(":")

        return Order(
            drink=self.DRINK_MATCHING[drink],
            sugars=0 if sugars is None else sugars,
            stick=False
        )

    def output_generator(self, order: Order) -> str:
        pass
