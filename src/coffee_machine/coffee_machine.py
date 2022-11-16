import dataclasses
from enum import Enum


class Drink(Enum):
    TEA = "tea"
    COFFEE = "coffee"
    HOT_CHOCOLATE = "hot chocolate"


@dataclasses.dataclass
class Order:
    drink: Drink
    sugars: int
    stick: bool


class CoffeeMachine:

    DRINK_MATCHING = {
        "T": Drink.TEA,
        "C": Drink.COFFEE,
        "H": Drink.HOT_CHOCOLATE,
    }

    def process(self, order_input: str) -> str:
        order = self.parser(order_input)
        output = self.output_generator(order)
        return output

    def parser(self, order: str) -> Order:
        drink, sugars, _ = order.split(":")

        return Order(
            drink=self.DRINK_MATCHING[drink], sugars=0 if sugars is "" else int(sugars), stick=False
        )

    def output_generator(self, order: Order) -> str:
        if order.sugars == 0:
            return f"Drink maker makes 1 {order.drink.value} with no sugar - and therefore no stick"
        return f"Drink maker makes 1 {order.drink.value} with {order.sugars} sugar{'s' if order.sugars > 1 else ''} and a stick"
