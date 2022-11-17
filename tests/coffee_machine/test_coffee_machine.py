from src.coffee_machine.coffee_machine import make_order

def test_make_tea():
    order = make_order("T", 1)
    assert order == "T:1:0"

def test_make_hot_chocolate():
    order = make_order("H", 0)
    assert order == "H::"
