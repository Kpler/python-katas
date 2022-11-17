import pytest

from src.coffee_machine.coffee_machine import CoffeeMachine, Order


def test_we_order_coffee():
    expected_order= "C::"
    order_input = Order("C")
    coffee_machine = CoffeeMachine()
    result = coffee_machine.generate_order(order_input)
    assert result == expected_order


def test_we_order_tea():
    expected_order= "T::"
    order_input = Order("T")
    coffee_machine = CoffeeMachine()
    result = coffee_machine.generate_order(order_input)
    assert result == expected_order


def test_we_order_hot_chocolate():
    expected_order= "H::"
    order_input = Order("H")
    coffee_machine = CoffeeMachine()
    result = coffee_machine.generate_order(order_input)
    assert result == expected_order


def test_we_order_drink_and_sugars_properly():
    expected_order= "H:2:0"
    order_input = Order("H", 2)
    coffee_machine = CoffeeMachine()
    result = coffee_machine.generate_order(order_input)
    assert result == expected_order