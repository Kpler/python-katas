import pytest
from coffee_machine.coffee_machine import DrinkMaker, Drink

@pytest.mark.parametrize(
    "drink_type, sugar, money, is_extra_hot, expected_output",
    [
        (Drink.CHOCOLATE, 1, 0.5, False, "H:1:0"),
        (Drink.COFFEE, 2, 1, False, "C:2:0"),
        (Drink.COFFEE, 0, 0.6, False, "C::"),
        (Drink.COFFEE, 3, 0.6, False, "M:no diabete"),
        (Drink.CHOCOLATE, 2, 0.1, False, "M:missing 0.4"),
        (Drink.CHOCOLATE, 1, 0.5, True, "Hh:1:0"),
        (Drink.ORANGE_JUICE, 0, 0.6, False, "O::"),
        (Drink.ORANGE_JUICE, 1, 0.6, False, "M:no sugar in orange juice"),
        (Drink.ORANGE_JUICE, 0, 0.6, True, "M:are you out of your mind"),
    ],
)
def test_drink_output(drink_type: Drink, sugar: int, money:float, is_extra_hot: bool, expected_output: str) -> None:
    drink_maker = DrinkMaker()
    result = drink_maker.make_drink(drink_type=drink_type, sugar=sugar, money=money,is_extra_hot=is_extra_hot)
    assert result == expected_output

