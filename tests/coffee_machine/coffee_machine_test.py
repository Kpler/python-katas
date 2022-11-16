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
        end_result = coffee_machine.add_sugar(result)
        self.assertEqual(end_result, "C:1:0")

    def test_when_making_chocolate_with_two_sugars_then_get_h_2_0(self):
        coffee_machine = CoffeeMachine()
        result = coffee_machine.make_chocolate()
        result_one_sugar = coffee_machine.add_sugar(result)
        result_two_sugar = coffee_machine.add_sugar(result_one_sugar)
        self.assertEqual(result_two_sugar, "H:2:0")

    def test_when_making_coffee_with_two_sugars_then_get_c_2_0(self):
        coffee_machine = CoffeeMachine()
        result = coffee_machine.make_coffee()
        result_one_sugar = coffee_machine.add_sugar(result)
        result_two_sugar = coffee_machine.add_sugar(result_one_sugar)
        self.assertEqual(result_two_sugar, "C:2:0")

    def test_when_making_coffee_with_three_sugars_then_get_c_2_0(self):
        coffee_machine = CoffeeMachine()
        result = coffee_machine.make_coffee()
        result_one_sugar = coffee_machine.add_sugar(result)
        result_two_sugar = coffee_machine.add_sugar(result_one_sugar)
        result_three_sugar = coffee_machine.add_sugar(result_two_sugar)
        self.assertEqual(result_three_sugar, "C:2:0")

    def test_when_display_message_return_message(self):
        coffee_machine = CoffeeMachine()
        result = coffee_machine.display_message()
        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
