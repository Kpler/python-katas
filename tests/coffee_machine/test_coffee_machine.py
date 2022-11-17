import pytest


class CoffeeMachine:
    def generate_order(self, drink_type:str):
        pass


def test_we_order_coffee():
    expected_order= "C::"
    coffee_machine = CoffeeMachine()
    result = coffee_machine.generate_order("c")
    assert result == expected_order