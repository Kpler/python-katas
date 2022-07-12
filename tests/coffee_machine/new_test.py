import pytest

from src.coffee_machine.drink_order import make_new_order, DrinkOrder


def test_tea_order_with_one_sugar():
    assert make_new_order(DrinkOrder("T", 1, 0)) == "T:1:0"


def test_coffee_order_with_one_sugar():
    assert make_new_order(DrinkOrder("C", 1, 0)) == "C:1:0"


def test_hot_chocolate_order_without_sugar_and_no_stick():
    assert make_new_order(DrinkOrder("H", 0, 0)) == "H::"
