from dataclasses import dataclass

EMPTY_ORDER = ""
TEA_ORDER = "T::"

@dataclass
class CoffeeMachine:

    order_beverage: str = None

    def get_order(self) -> str:
        if self.order_beverage == 'tea':
            return TEA_ORDER
        return EMPTY_ORDER
    
    def send_order(self, beverage: str) -> None:
        self.order_beverage = beverage