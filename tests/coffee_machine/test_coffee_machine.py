import pytest

from src.coffee_machine.coffee_machine import CoffeeMachine, Order, DrinkType


def test_we_order_coffee():
    expected_order= "C::"
    drink_type = DrinkType.COFFEE
    order_input = Order(drink_type=drink_type, money=1)
    coffee_machine = CoffeeMachine()
    result = coffee_machine.generate_order(order_input)
    assert result == expected_order


def test_we_order_tea():
    expected_order= "T::"
    drink_type = DrinkType.TEA
    order_input = Order(drink_type=drink_type, money=1)
    coffee_machine = CoffeeMachine()
    result = coffee_machine.generate_order(order_input)
    assert result == expected_order


def test_we_order_hot_chocolate():
    expected_order= "H::"
    drink_type = DrinkType.HOT_CHOCOLATE
    order_input = Order(drink_type=drink_type, money=1)
    coffee_machine = CoffeeMachine()
    result = coffee_machine.generate_order(order_input)
    assert result == expected_order


def test_we_order_drink_and_sugars_properly():
    expected_order= "H:2:0"
    drink_type = DrinkType.HOT_CHOCOLATE
    order_input = Order(drink_type=drink_type, sugars=2, money=1)
    coffee_machine = CoffeeMachine()
    result = coffee_machine.generate_order(order_input)
    assert result == expected_order


def test_order_coffee_with_money():
    expected_result = "M:message-content"
    drink_type = DrinkType.HOT_CHOCOLATE
    order_input = Order(drink_type=drink_type, sugars=2)
    coffee_machine = CoffeeMachine()
    result = coffee_machine.generate_order(order_input)
    assert result == expected_result


def test_order_coffee_with_not_enough_money():
    expected_result = "M:message-content"
    drink_type = DrinkType.HOT_CHOCOLATE
    order_input = Order(drink_type=drink_type, sugars=2, money=0.4)
    coffee_machine = CoffeeMachine()
    result = coffee_machine.generate_order(order_input)
    assert result == expected_result







