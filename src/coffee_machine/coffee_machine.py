def order(order_type: str, nb_of_sugars: int = 0) -> str:
    if order_type == 'H':
        return 'H::'
    elif order_type == 'T':
        return 'T::'
    elif order_type == 'C':
        return 'C::'
    else:
        return 'M:Unsupported Drink'
