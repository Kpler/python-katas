from src.coffee_machine.foo import is_valid_order

def test_1():
    assert is_valid_order("") is False


def test_2():
    assert is_valid_order("::") is False


def test_order_tea():
    assert is_valid_order("T::") is True


def test_order_chocolate():
    assert is_valid_order("H::") is True


def test_order_coffee():
    assert is_valid_order("C::") is True
