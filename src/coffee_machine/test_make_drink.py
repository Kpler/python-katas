from src.coffee_machine.make_drink import make_drink


def test_coffee():
  assert make_drink("coffee") == 'C::'
  
def test_coffee_with_sugar():
  assert make_drink("coffee", 1) == 'C:1:1'