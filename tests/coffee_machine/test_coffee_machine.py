from src.coffee_machine.coffee_machine import CoffeeMachine


def test_coffee_machine():
    machine_input = "T::"
    expected_output = "Drink maker makes 1 tea with no sugar - and therefore no stick"

    machine = CoffeeMachine()
    machine_output = machine.process(machine_input)

    assert machine_output == expected_output