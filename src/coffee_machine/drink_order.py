from dataclasses import dataclass


@dataclass
class DrinkOrder:
    drink_type: str
    num_sugar: int
    stick: int


def make_new_order(order: DrinkOrder):
    num_sugar_processed = order.num_sugar if order.num_sugar > 0 else ""

    if num_sugar_processed == "":
        stick_processed = ""
    elif order.stick > 0:
        stick_processed = order.stick
    else:
        stick_processed = ""

    result = f"{order.drink_type}:{num_sugar_processed}:{stick_processed}"
    return result
