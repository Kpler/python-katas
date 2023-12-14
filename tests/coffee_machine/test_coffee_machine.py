from src.coffee_machine.coffee_machine import CoffeeMachine


def test_coffee_machine_can_instantiate_itself():
    coffe_machine = CoffeeMachine()


def test_should_return_an_empty_string_when_no_order_passed():
    coffee_machine = CoffeeMachine()
    order = coffee_machine.get_order()
    assert order == ""


def test_should_return_tea_order_when_order_a_beverage_is_tea():
    coffee_machine = CoffeeMachine()
    coffee_machine.send_order(beverage='tea')
    order = coffee_machine.get_order()
    assert order == "T::"


def test_should_return_coffee_order_when_order_a_beverage_is_coffee():
    coffee_machine = CoffeeMachine()
    coffee_machine.send_order(beverage='coffee')
    order = coffee_machine.get_order()
    assert order == "C::"


def test_should_return_chocolate_order_when_order_a_beverage_is_chocolate():
    coffee_machine = CoffeeMachine()
    coffee_machine.send_order(beverage='hot_chocolate')
    order = coffee_machine.get_order()
    assert order == "H::"