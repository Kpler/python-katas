from src.coffee_machine.coffee_machine import CoffeeMachine, CoffeeMachineException, Drink
import pytest

@pytest.mark.parametrize(
    "drink,number_of_sugars,money, expected_message",
    [
        (Drink.CHOCOLATE, 1, 0, "H:1:0"),
        (Drink.TEA, 0, 0, "T::"),
        (Drink.COFFEE, 2, 0, "C:2:0"),
        (Drink.COFFEE, 3, 0, "M:Don't take too much sugar. It's bad for your health!"),
    ]
)
def test_make_drink(drink: str, number_of_sugars: int, money: float, expected_message: str) -> None:
    # GIVEN
    coffee_machine = CoffeeMachine()
    # WHEN
    message = coffee_machine.order_drink(drink, number_of_sugars, money)
    # THEN
    assert message == expected_message

def test_invalid_drink() -> None:
    # GIVEN
    coffee_machine = CoffeeMachine()
    # WHEN / THEN
    with pytest.raises(CoffeeMachineException):
        coffee_machine.order_drink("invalid_drink", 0, 0)

