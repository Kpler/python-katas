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



def test_sugar():
    drink_maker = DrinkMaker()
    command = drink_maker.make(order=Beverage.TEA, sugar=1)
    assert command == "T:1:0"