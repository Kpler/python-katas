from src.coffee_machine.foo import make_order, Drink

def test_1():
    assert make_order("") is None


def test_2():
    assert make_order("::") is None


def test_order_tea():
    assert make_order("T::") == Drink("tea", 0, False)


def test_order_chocolate():
    assert make_order("H::") == Drink("chocolate", 0, False)


def test_order_chocolate_with_sugar():
    assert make_order("H:1:") == Drink("chocolate", 1, True)


def test_order_chocolate_with_too_many_sugar():
    assert make_order("H:6:") is None


def test_order_coffee():
    assert make_order("C::") == Drink("coffee", 0, False)


def test_improper_stick():
    assert make_order("T::0") is None
