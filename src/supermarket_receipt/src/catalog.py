from src.model_objects import Product


class SupermarketCatalog:
    def __init__(self):
        self.products: dict[str, Product] = {}
        self.prices: dict[str, float] = {}

    def add_product(self, product: Product, price: float) -> None:
        raise Exception("cannot be called from a unit test - it accesses the database")

    def unit_price(self, product: Product) -> float:
        raise Exception("cannot be called from a unit test - it accesses the database")
