from enum import Enum


class Beverage(Enum):
    TEA = "Tea"
    COFFEE = "Coffee"
    HOT_CHOCOLATE = "Hot Chocolate"


class DrinkMaker:
    def make(self, order: Beverage | str, sugar: int = 0) -> str:
        sugar_output = ":" if sugar == 0 else f"{sugar}:0"
        if order == Beverage.TEA:
            command = f"T:{sugar_output}"
        elif order == Beverage.HOT_CHOCOLATE:
            command = f"H:{sugar_output}"
        elif order == Beverage.COFFEE:
            command = f"C:{sugar_output}"
        else:
            command = f"M:{order}"
        return command
