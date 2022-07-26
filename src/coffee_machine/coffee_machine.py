def order(order_type: str, nb_of_sugars: int = 0):
    if order_type == 'H':
        return 'H::'
    else:
        return 'T::'

