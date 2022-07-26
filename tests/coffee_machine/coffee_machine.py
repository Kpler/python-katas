from src.coffee_machine.coffee_machine import order


def test_should_order_simple_hot_chocolate():
    result = order('H')
    assert result == 'H::'

def test_should_order_simple_tea():
    result = order('T')
    assert result == 'T::'

def test_should_order_simple_coffee():
    result = order('C')
    assert result == 'C::'

def test_should_not_order_anything_if_not_a_tea_coffee_hot_chocolate():
    result = order('')
    assert result == 'M:Unsupported Drink'

# def test_should_order_simple_coffee():
#     result = order('C')
#     assert result == 'C::'
