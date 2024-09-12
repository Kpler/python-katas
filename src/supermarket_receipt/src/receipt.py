from src.model_objects import Discount, Product


class ReceiptItem:
    def __init__(self, product: Product, quantity: float, price: float, total_price: float) -> None:
        self.product = product
        self.quantity = quantity
        self.price = price
        self.total_price = total_price


class Receipt:
    def __init__(self) -> None:
        self._items: list[ReceiptItem] = []
        self._discounts: list[Discount] = []

    def total_price(self) -> float:
        total = 0
        for item in self.items:
            total += item.total_price
        for discount in self.discounts:
            total += discount.discount_amount
        return total

    def add_product(self, product: Product, quantity: float, price: float, total_price: float) -> None:
        self._items.append(ReceiptItem(product, quantity, price, total_price))

    def add_discount(self, discount: Discount) -> None:
        self._discounts.append(discount)

    @property
    def items(self) -> list[ReceiptItem]:
        return self._items[:]

    @property
    def discounts(self) -> list[Discount]:
        return self._discounts[:]
