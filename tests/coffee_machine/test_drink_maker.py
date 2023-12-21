import pytest

from src.coffee_machine.drink_maker import DrinkMaker, Beverage


@pytest.mark.parametrize(
    "input,output",
    [
        [Beverage.TEA, "T::"],
        [Beverage.HOT_CHOCOLATE, "H::"],
        [Beverage.COFFEE, "C::"],
        ["Hello World", "M:Hello World"],
    ],
)
def test_make_tea(
    input,
    output,
):
    drink_maker = DrinkMaker()
    command = drink_maker.make(order=input)
    assert command == output


@pytest.mark.parametrize(
    "sugar,output",
    [
        [1, "T:1:0"],
        [2, "T:2:0"],
    ],
)
def test_sugar(sugar, output):
    drink_maker = DrinkMaker()
    command = drink_maker.make(order=Beverage.TEA, sugar=sugar)
    assert command == output


@pytest.mark.parametrize(
    "order,sugar,amount,output",
    [
        [Beverage.TEA, 0, 0.3, "M:Missing 0.1"],
        [Beverage.TEA, 0, 0.4, "T::"],
        [Beverage.COFFEE, 0, 0.5, "C::"],
    ],
)
def test_money(order,
               sugar,
               amount,
               output):
    drink_maker = DrinkMaker()
    command = drink_maker.make(order=order, sugar=sugar, amount=amount)
    assert command == output


