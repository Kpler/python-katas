import unittest
from enum import Enum


class DrinkType(Enum):
    TEA = 1
    COFFEE = 2
    CHOCOLATE = 3

    def to_drink_maker_protocol(self):
        match self:
            case DrinkType.TEA:
                return 'T'
            case DrinkType.COFFEE:
                return 'C'
            case DrinkType.CHOCOLATE:
                return 'H'


class CoffeeTestCase(unittest.TestCase):
    def test_tea_order(self):
        # GIVEN
        drink_type = DrinkType.TEA
        sugar = 1
        # WHEN
        result = self.make_order(drink_type, sugar)
        # THEN
        self.assertEqual(result, "T:1:0")  # add assertion here

    def test_no_sugar_order(self):
        drink_type = DrinkType.CHOCOLATE
        sugar = 0
        result = self.make_order(drink_type, sugar)
        self.assertEqual(result, "H::")


    def make_order(self, drink_type: DrinkType, sugar: int):
        sugar_str = str(sugar) if sugar > 0 else ''
        stick = '0' if sugar > 0 else ''
        return ':'.join([drink_type.to_drink_maker_protocol(), sugar_str, stick])


if __name__ == '__main__':
    unittest.main()