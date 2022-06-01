from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class Drink:
    kind: str
    sugar: int
    stick: bool


def make_order(order: str) -> Optional[Drink]:
    """
    Returns: None when the order is invalid
    """
    parts = order.split(":")

    # Validation
    if len(parts) != 3:
        return None

    if parts[0] not in {"T", "H", "C"}:
        return None

    if parts[1] not in {"", "1", "2"}:
        return None

    # Make the drink
    sugar: int = int(parts[1] or "0")
    stick: bool = sugar > 0

    match parts[0]:
        case "T":
            drink = Drink("tea", sugar, stick)
        case "H":
            drink = Drink("chocolate", sugar, stick)
        case "C":
            drink = Drink("coffee", sugar, stick)
            
    return drink
