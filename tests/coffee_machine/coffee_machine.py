from src.coffee_machine.coffee_machine import order


def test_should_order_simple_hot_chocolate():
    result = order('H')
    assert result is 'H::'

def test_should_order_simple_tea():
    result = order('T')
    assert result is 'T::'

