from src.model_objects import Offer, Product, SpecialOfferType
from src.catalog import SupermarketCatalog
from src.receipt import Receipt
from src.shopping_cart import ShoppingCart


class Teller:

    def __init__(self, catalog: SupermarketCatalog) -> None:
        self.catalog: SupermarketCatalog = catalog
        self.offers: dict[Product, Offer] = {}

    def add_special_offer(self, offer_type: SpecialOfferType, product: Product, argument: float) -> None:
        self.offers[product] = Offer(offer_type, product, argument)

    def checks_out_articles_from(self, the_cart: ShoppingCart) -> Receipt:
        receipt = Receipt()
        product_quantities = the_cart.items
        for pq in product_quantities:
            p = pq.product
            quantity = pq.quantity
            unit_price = self.catalog.unit_price(p)
            price = quantity * unit_price
            receipt.add_product(p, quantity, unit_price, price)

        the_cart.handle_offers(receipt, self.offers, self.catalog)

        return receipt

    def product_with_name(self, name: str):
        return self.catalog.products.get(name, None)
