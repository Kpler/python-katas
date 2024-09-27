import math

from src.model_objects import ProductQuantity, SpecialOfferType, Discount


def get_discount_two_for_amount(
    quantity_as_int,
    offer,
    unit_price,
    p,
    quantity,
):
    discount = None
    if quantity_as_int >= 2:
        total = offer.argument * (quantity_as_int / 2) + quantity_as_int % 2 * unit_price
        discount_n = unit_price * quantity - total
        discount = Discount(p, "2 for " + str(offer.argument), -discount_n)
    return discount


class ShoppingCart:
    def __init__(self):
        self._items = []
        self._product_quantities = {}

    @property
    def items(self):
        return self._items

    def add_item(self, product):
        self.add_item_quantity(product, 1.0)

    @property
    def product_quantities(self):
        return self._product_quantities

    def add_item_quantity(self, product, quantity):
        self._items.append(ProductQuantity(product, quantity))
        if product in self._product_quantities.keys():
            self._product_quantities[product] = self._product_quantities[product] + quantity
        else:
            self._product_quantities[product] = quantity

    def handle_offers(self, receipt, offers, catalog):
        offer_type_nr_mapping = {
            SpecialOfferType.THREE_FOR_TWO: 3,
            SpecialOfferType.TWO_FOR_AMOUNT: 2,
            SpecialOfferType.FIVE_FOR_AMOUNT: 5,
            SpecialOfferType.TEN_PERCENT_DISCOUNT: 1,
            # TODO: Check whether offer_type can be None.
            # If not: Remove this dict entry.
            None: 1,
        }
        for p in self._product_quantities.keys():
            quantity = self._product_quantities[p]
            if p in offers.keys():
                offer = offers[p]
                unit_price = catalog.unit_price(p)
                quantity_as_int = int(quantity)
                discount = None
                offer_dependent_magic_number = offer_type_nr_mapping[offer.offer_type]

                if offer.offer_type == SpecialOfferType.TWO_FOR_AMOUNT:
                    discount = get_discount_two_for_amount(
                        quantity_as_int,
                        offer,
                        unit_price,
                        p,
                        quantity,
                    )

                number_of_x = math.floor(quantity_as_int / offer_dependent_magic_number)
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
                    discount = Discount(
                        p,
                        str(offer_dependent_magic_number) + " for " + str(offer.argument),
                        -discount_total,
                    )

                if discount:
                    receipt.add_discount(discount)
        return receipt
