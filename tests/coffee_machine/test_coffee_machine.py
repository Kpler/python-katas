from src.coffee_machine.coffee_machine import make_order, DrinkType

def test_make_tea():
    order = make_order(DrinkType.TEA, 1)
    assert order == "T:1:0"

def test_make_hot_chocolate():
    order = make_order(DrinkType.HOT_CHOCOLATE, 0)
    assert order == "H::"

def test_not_make_hot_chocolate():
    order = make_order(DrinkType.TEA, 0)
    assert not order == "H::"
