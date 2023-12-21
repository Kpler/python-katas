from enum import Enum


class Beverage(Enum):
    TEA = "Tea"
    COFFEE = "Coffee"
    HOT_CHOCOLATE = "Hot Chocolate"


class DrinkMaker:
    def make(
        self,
        drink: Beverage,
    ) -> str:
        if drink == Beverage.TEA:
            command = "T::"
        elif drink == Beverage.HOT_CHOCOLATE:
            command = "H::"
        elif drink == Beverage.COFFEE:
            command = "C::"

        return command
