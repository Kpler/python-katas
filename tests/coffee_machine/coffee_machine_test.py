import unittest


class CoffeeMachine:
    def make_tea(self) -> str:
        return "T::"


class CoffeeMachineTestCase(unittest.TestCase):
    def test_when_making_tea_then_get_tea_1_0(self):
        coffee_machine = CoffeeMachine()
        result = coffee_machine.make_tea()
        self.assertEqual(result, "T::")  # add assertion here


if __name__ == "__main__":
    unittest.main()
