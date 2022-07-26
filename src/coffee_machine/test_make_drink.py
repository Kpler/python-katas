from src.coffee_machine.make_drink import make_drink
import pytest

def test_coffee():
  assert make_drink("coffee") == 'C::'
  
def test_coffee_with_sugar():
  assert make_drink("coffee", 1) == 'C:1:1'

def test_super_sugary_chocolate():
  assert make_drink("chocolate", 10) == 'H:10:1'

def test_negative_sugar():
  with pytest.raises(Exception):
    make_drink("tea", -3) 

