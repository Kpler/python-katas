import math

from src.catalog import SupermarketCatalog
from src.model_objects import Offer, Product, SpecialOfferType, Discount
from src.receipt import Receipt
from src.shopping_cart import ShoppingCart

OfferMap = dict[Product, Offer]


class Teller:
    """The entity scanning the item."""

    def __init__(self, catalog: SupermarketCatalog) -> None:
        self.catalog: SupermarketCatalog = catalog
        self.offers: OfferMap = {}

    def add_special_offer(self, offer_type: SpecialOfferType, product: Product, argument: float):
        self.offers[product] = Offer(offer_type, product, argument)

    @staticmethod
    def handle_offers(cart, receipt, offers, catalog):
        for p in cart._product_quantities.keys():
            quantity = cart._product_quantities[p]
            if p in offers.keys():
                offer = offers[p]
                unit_price = catalog.unit_price(p)
                quantity_as_int = int(quantity)
                discount = None
                x = 1
                if offer.offer_type == SpecialOfferType.THREE_FOR_TWO:
                    x = 3

                elif offer.offer_type == SpecialOfferType.TWO_FOR_AMOUNT:
                    x = 2
                    if quantity_as_int >= 2:
                        total = (
                            offer.argument * (quantity_as_int / x)
                            + quantity_as_int % 2 * unit_price
                        )
                        discount_n = unit_price * quantity - total
                        discount = Discount(p, "2 for " + str(offer.argument), -discount_n)

                if offer.offer_type == SpecialOfferType.FIVE_FOR_AMOUNT:
                    x = 5

                number_of_x = math.floor(quantity_as_int / x)
                if offer.offer_type == SpecialOfferType.THREE_FOR_TWO and quantity_as_int > 2:
                    discount_amount = quantity * unit_price - (
                        (number_of_x * 2 * unit_price) + quantity_as_int % 3 * unit_price
                    )
                    discount = Discount(p, "3 for 2", -discount_amount)

                if offer.offer_type == SpecialOfferType.TEN_PERCENT_DISCOUNT:
                    discount = Discount(
                        p,
                        str(offer.argument) + "% off",
                        -quantity * unit_price * offer.argument / 100.0,
                    )

                if offer.offer_type == SpecialOfferType.FIVE_FOR_AMOUNT and quantity_as_int >= 5:
                    discount_total = unit_price * quantity - (
                        offer.argument * number_of_x + quantity_as_int % 5 * unit_price
                    )
                    discount = Discount(p, str(x) + " for " + str(offer.argument), -discount_total)

                if discount:
                    receipt.add_discount(discount)

    def checks_out_articles_from(self, the_cart: ShoppingCart) -> Receipt:
        receipt = Receipt()

        product_quantities = the_cart.items
        for pq in product_quantities:
            p = pq.product
            quantity = pq.quantity
            unit_price = self.catalog.unit_price(p)
            price = quantity * unit_price
            receipt.add_product(p, quantity, unit_price, price)

        self.handle_offers(the_cart, receipt, self.offers, self.catalog)

        return receipt
