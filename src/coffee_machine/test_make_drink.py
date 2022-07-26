from src.coffee_machine.make_drink import make_drink


def test_coffee():
  assert make_drink("coffee") is "C::"