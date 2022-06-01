def is_valid_order(order: str) -> bool:
    parts = order.split(":")

    if len(parts) != 3:
        return False

    if parts[0] in {"T", "H", "C"}:
        return True

    return False
