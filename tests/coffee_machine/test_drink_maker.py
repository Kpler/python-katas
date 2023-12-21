import pytest

from src.coffee_machine.drink_maker import DrinkMaker, Beverage


@pytest.mark.parametrize(
    "input,output",
    [
        [Beverage.TEA, "T::"],
        [Beverage.HOT_CHOCOLATE, "H::"],
        [Beverage.COFFEE, "C::"],
    ],
)
def test_make_tea(
    input,
    output,
):
    drink_maker = DrinkMaker()
    command = drink_maker.make(drink=input)
    assert command == output
