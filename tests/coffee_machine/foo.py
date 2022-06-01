from src.coffee_machine.foo import is_valid_order

def test_1():
    assert is_valid_order("") is False
