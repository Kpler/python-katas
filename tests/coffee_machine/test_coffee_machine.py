from src.coffee_machine.coffee_machine import CoffeeMachine


def test_init():
    coffee_machine = CoffeeMachine()

    assert coffee_machine


def test_order_tea():
    coffee_machine = CoffeeMachine()
    assert coffee_machine.order(drink_type="Tea", sugar=1, money=0.4) == "T:1:0"


def test_order_tea_without_sugar():
    coffee_machine = CoffeeMachine()
    assert (
        coffee_machine.order(
            drink_type="Tea",
            sugar=0,
            money=0.4,
        )
        == "T::"
    )


def test_order_chocolate():
    coffee_machine = CoffeeMachine()
    assert (
        coffee_machine.order(
            drink_type="Chocolate",
            sugar=0,
            money=0.6,
        )
        == "H::"
    )


def test_order_coffee():
    coffee_machine = CoffeeMachine()
    assert (
        coffee_machine.order(
            drink_type="Coffee",
            sugar=2,
            money=0.6
        )
        == "C:2:0"
    )


def test_message_content():
    coffee_machine = CoffeeMachine()
    assert coffee_machine.print_message("message") == "M:message"
