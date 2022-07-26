from enum import Enum


class DrinkType(Enum):
    TEA = 1
    COFFEE = 2
    CHOCOLATE = 3

    def to_drink_maker_protocol(self) -> str:
        match self:
            case DrinkType.TEA:
                return 'T'
            case DrinkType.COFFEE:
                return 'C'
            case DrinkType.CHOCOLATE:
                return 'H'

    def to_price(self) -> float:
        match self:
            case DrinkType.TEA:
                return 0.4
            case DrinkType.COFFEE:
                return 0.6
            case DrinkType.CHOCOLATE:
                return 0.5


def make_order(drink_type: DrinkType, sugar: int, money: float):
    sugar_str = str(sugar) if sugar > 0 else ''
    stick = '0' if sugar > 0 else ''

    if drink_type.to_price() > money:
        return "M:missing 0.4 euros"

    return ':'.join([drink_type.to_drink_maker_protocol(), sugar_str, stick])
