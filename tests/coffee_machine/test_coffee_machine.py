import pytest

from src.coffee_machine.coffee_machine import CoffeeMachine


@pytest.mark.parametrize(
    ["machine_input", "expected_output"],
    [
        ("T::", "Drink maker makes 1 tea with no sugar - and therefore no stick"),
        ("H::", "Drink maker makes 1 hot chocolate with no sugar - and therefore no stick"),
        ("C::", "Drink maker makes 1 coffee with no sugar - and therefore no stick"),
    ],
)
def test_coffee_machine_without_sugar(machine_input, expected_output):
    machine = CoffeeMachine()
    machine_output = machine.process(machine_input)

    assert machine_output == expected_output


@pytest.mark.parametrize(
    ["machine_input", "expected_output"],
    [
        ("T:1:0", "Drink maker makes 1 tea with 1 sugar and a stick"),
        ("T:2:0", "Drink maker makes 1 tea with 2 sugars and a stick"),
    ],
)
def test_coffee_machine_with_sugar(machine_input, expected_output):
    machine = CoffeeMachine()
    machine_output = machine.process(machine_input)

    assert machine_output == expected_output
