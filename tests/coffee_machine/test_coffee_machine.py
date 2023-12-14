from src.coffee_machine.coffee_machine import CoffeeMachine


def test_init():
    coffee_machine = CoffeeMachine()

    assert coffee_machine


def test_order_tea():
    coffee_machine = CoffeeMachine()
    assert coffee_machine.order(
        drink_type="Tea",
        sugar=1
    ) == "T:1:0"

def test_order_tea_without_sugar():
    # TODO
    pass