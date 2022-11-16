import unittest

from src.coffee_machine.coffee_machine import CoffeeMachine


class CoffeeMachineTestCase(unittest.TestCase):
    def test_when_making_tea_then_get_t_colon_colon(self):
        coffee_machine = CoffeeMachine()
        result = coffee_machine.make_tea()
        self.assertEqual(result, "T::")

    def test_when_making_coffee_then_get_c_colon_colon(self):
        coffee_machine = CoffeeMachine()
        result = coffee_machine.make_coffee()
        self.assertEqual(result, "C::")

    def test_when_making_chocolate_then_get_h_colon_colon(self):
        coffee_machine = CoffeeMachine()
        result = coffee_machine.make_chocolate()
        self.assertEqual(result, "H::")

    def test_when_making_coffee_with_one_sugar_then_get_c_1_0(self):
        coffee_machine = CoffeeMachine()
        result = coffee_machine.make_coffee()
        end_result = coffee_machine.add_sugar(1, result)
        self.assertEqual(end_result, "C:1:0")

if __name__ == "__main__":
    unittest.main()
