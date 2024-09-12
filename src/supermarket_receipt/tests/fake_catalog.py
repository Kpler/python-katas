from src.catalog import SupermarketCatalog
from src.model_objects import Product


class FakeCatalog(SupermarketCatalog):
    def add_product(self, product: Product, price: float) -> None:
        self.products[product.name] = product
        self.prices[product.name] = price

    def unit_price(self, product: Product) -> float:
        return self.prices[product.name]
