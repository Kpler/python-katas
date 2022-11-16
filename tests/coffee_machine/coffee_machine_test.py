import unittest


class CoffeMachine:
    pass


class CoffeeMachineTestCase(unittest.TestCase):
    coffee_machine = CoffeMachine()

    def when_making_tea_then_get_tea_1_0(self):
        coffee_machine.make_tea()
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
