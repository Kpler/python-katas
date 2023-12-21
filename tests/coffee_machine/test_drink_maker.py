import pytest

from src.coffee_machine.drink_maker import DrinkMaker


@pytest.mark.parametrize(
    "input,output",
    [
        ["Tea", "T::"],
        ["Hot Chocolate", "H::"],
    ],
)
def test_make_tea(
    input,
    output,
):
    drink_maker = DrinkMaker()
    command = drink_maker.make(drink=input)
    assert command == output
