from enum import Enum


class Beverage(Enum):
    TEA = "Tea"
    COFFEE = "Coffee"
    HOT_CHOCOLATE = "Hot Chocolate"


class DrinkMaker:
    def make(
        self,
        order: Beverage | str,
        sugar: int = 0
    ) -> str:
        
        if order == Beverage.TEA:
            command = "T::"

        if order == Beverage.TEA:
            command = "T::"
        elif order == Beverage.HOT_CHOCOLATE:
            command = "H::"
        elif order == Beverage.COFFEE:
            command = "C::"
        else:
            command = f"M:{order}"

        return command
