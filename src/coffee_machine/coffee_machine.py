from dataclasses import dataclass

EMPTY_ORDER = ""

@dataclass
class CoffeeMachine:

    def get_order(self) -> str:
        return EMPTY_ORDER