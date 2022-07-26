def order(order_type: str, nb_of_sugars: int = 0):
    return 'H::'


def test_should_order_simple_hot_chocolate():
    result = order('H')
    assert result is 'H::'

def test_should_order_simple_tea():
    result = order('T')
    assert result is 'T::'

