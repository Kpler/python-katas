from dataclasses import dataclass


@dataclass
class DrinkOrder:
    drink_type: str
    num_sugar: int
    stick: int


def make_new_order(order: DrinkOrder):

    result = f"{order.drink_type}:{order.num_sugar}:{order.stick}"
    return result
