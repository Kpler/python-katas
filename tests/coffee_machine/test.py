from src.coffee_machine.coffee_machine import CoffeeMachine


def test_init():
    coffee_machine = CoffeeMachine()

    assert coffee_machine
