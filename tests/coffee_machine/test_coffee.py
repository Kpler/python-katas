import unittest

from src.coffee_machine.coffee_machine import DrinkType, make_order


class CoffeeTestCase(unittest.TestCase):
    def test_tea_order(self):
        # GIVEN
        drink_type = DrinkType.TEA
        sugar = 1
        money = 0.4
        # WHEN
        result = make_order(drink_type, sugar, money)
        # THEN
        self.assertEqual(result, "T:1:0")

    def test_no_sugar_order(self):
        drink_type = DrinkType.CHOCOLATE
        sugar = 0
        money = 0.5
        result = make_order(drink_type, sugar, money)
        self.assertEqual(result, "H::")

    def test_not_enough_money(self):
        result = make_order(DrinkType.CHOCOLATE, 0, 0.3)
        self.assertEqual(result, "M:missing 0.2 euros")

