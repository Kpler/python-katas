def is_valid_order(order: str) -> bool:
    parts = order.split(":")

    if len(parts) != 3:
        return False

    if parts[0] not in {"T", "H", "C"}:
        return False
    if parts[1] not in {None, str(1), str(2)}:
        return False

    return True
