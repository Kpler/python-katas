from src.coffee_machine.coffee_machine import CoffeeMachine


def test_init():
    coffee_machine = CoffeeMachine()

    assert coffee_machine


def test_order_tea():
    coffee_machine = CoffeeMachine()
    assert coffee_machine.order("T::") == ("Drink maker makes 1 tea with no sugar - "
                                           "and therefore no stick")


def test_order_tea_with_sugar():
    coffee_machine = CoffeeMachine()
    assert coffee_machine.order("T:1:0") == ("Drink maker makes 1 tea "
                                             "with 1 sugar and a stick")
