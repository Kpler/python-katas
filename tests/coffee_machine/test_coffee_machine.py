from typing import Any

import pytest

from src.coffee_machine.coffee_machine import CoffeeMaker, DrinkType

@pytest.mark.parametrize(
    "given,expected",
    [
        ({"drink_type":DrinkType.Tea, "nb_of_sugar": 1, "money": 1.0}, "T:1:0"),
        ({"drink_type":DrinkType.Coffee, "nb_of_sugar": 0, "money": 1.0}, "C::"),
        ({"drink_type":DrinkType.Chocolate, "nb_of_sugar": 0, "money": 1.0}, "H::"),
        ({"drink_type":DrinkType.Chocolate, "nb_of_sugar": 2, "money": 1.0}, "H:2:0"),
        ({"drink_type":DrinkType.Chocolate, "nb_of_sugar": 3, "money": 1.0}, "M:sugar-is-not-good-for-your-health"),
        ({"drink_type":DrinkType.OrangeJuice, "money": 1.0}, "O::"),
        ({"drink_type":DrinkType.Tea, "nb_of_sugar": 1, "money": 1.0, "extra_hot": True}, "Th:1:0"),
        ({"drink_type":DrinkType.Tea, "nb_of_sugar": 1, "money": 0.3}, "M:you-miss-0.1-EURO-to-make-a-drink"),
        ({"drink_type":DrinkType.Coffee, "nb_of_sugar": 1, "money": 0.1}, "M:you-miss-0.5-EURO-to-make-a-drink"),
        ({"drink_type":DrinkType.Chocolate, "nb_of_sugar": 1, "money": 0.2}, "M:you-miss-0.3-EURO-to-make-a-drink"),
        ({"drink_type":DrinkType.OrangeJuice, "money": 0.5}, "M:you-miss-0.1-EURO-to-make-a-drink"),
        ({"drink_type":DrinkType.OrangeJuice, "nb_of_sugar": 1, "money": 0.6}, "M:do-not-put-sugar-in-your-orange-juice"),
        ({"drink_type":DrinkType.OrangeJuice, "extra_hot": True, "money": 0.6}, "M:do-not-make-hot-orange-juice"),
    ]
)
def test_make_drink(given: dict[str, Any], expected: str) -> None:
    coffee_maker = CoffeeMaker()
    assert coffee_maker.make_drink(**given) == expected

def test_get_report():
    coffee_maker = CoffeeMaker()
    assert coffee_maker.get_report() == {
        DrinkType.Coffee: 0,
        DrinkType.Chocolate: 0,
        DrinkType.Tea: 0,
        DrinkType.OrangeJuice: 0,
        "money": 0
    }

def test_get_report_sold_tea():
    coffee_maker = CoffeeMaker()
    coffee_maker.make_drink(drink_type=DrinkType.Tea, money=1.0)
    assert coffee_maker.get_report() == {
        DrinkType.Coffee: 0,
        DrinkType.Chocolate: 0,
        DrinkType.Tea: 1,
        DrinkType.OrangeJuice: 0,
        "money": 1,
    }