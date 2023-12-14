from src.coffee_machine.coffee_machine import CoffeeMachine


def test_init():
    coffee_machine = CoffeeMachine()

    assert coffee_machine


def test_order_tea():
    coffee_machine = CoffeeMachine()
    assert coffee_machine.order() == "T::"


def test_order_tea_with_sugar():
    coffee_machine = CoffeeMachine()
    assert coffee_machine.order() == "T:1:0"
