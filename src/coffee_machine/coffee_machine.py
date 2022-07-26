def order(order_type: str, nb_of_sugars: int = 0, nb_of_stick: int = 0) -> str:
    if order_type == 'H':
        return 'H::'
    elif order_type == 'T':
        if nb_of_sugars > 0:
            return f"T:{nb_of_sugars}:{nb_of_stick}"
        return 'T::'
    elif order_type == 'C':
        if nb_of_sugars > 0:
            return f"C:{nb_of_sugars}:{nb_of_stick}"
        return 'C::'
    else:
        return 'M:Unsupported Drink'
