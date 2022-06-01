from typing import Optional
from dataclasses import dataclass

@dataclass(frozen=True)
class Drink:
    kind: str
    sugar: int
    stick: bool

def make_order(order: str) -> Optional[Drink]:
    parts = order.split(":")

    if len(parts) != 3:
        return None

    if parts[0] not in {"T", "H", "C"}:
        return None

    if parts[1] not in {"", "1", "2"}:
        return None

    if parts[2] and parts[1] == "":
        return None

    sugar = int(parts[1] or "0")
    match parts[0]:
        case "T":
            drink = Drink(kind="tea", sugar, False)
        case "H":
            drink = Drink("chocolate", sugar, False)
        case "C":
            drink = Drink("coffee", sugar, False)
    return drink
