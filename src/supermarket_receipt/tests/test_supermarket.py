import approvaltests

from src.model_objects import SpecialOfferType, Product
from tests.receipt_printer import ReceiptPrinter

from src.teller import Teller
from src.shopping_cart import ShoppingCart


def test_empty_basket(teller: Teller, cart: ShoppingCart, toothbrush: Product, apples: Product) -> None:
    receipt = teller.checks_out_articles_from(cart)

    approvaltests.verify(ReceiptPrinter().print_receipt(receipt))


def test_no_discount(teller: Teller, cart: ShoppingCart, toothbrush: Product, apples: Product) -> None:
    teller.add_special_offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, toothbrush, 10.0)
    cart.add_item_quantity(apples, 2.5)

    receipt = teller.checks_out_articles_from(cart)

    approvaltests.verify(ReceiptPrinter().print_receipt(receipt))


def test_ten_percent_discount(teller: Teller, cart: ShoppingCart, toothbrush: Product) -> None:
    teller.add_special_offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, toothbrush, 10.0)
    cart.add_item_quantity(toothbrush, 2)

    receipt = teller.checks_out_articles_from(cart)

    approvaltests.verify(ReceiptPrinter().print_receipt(receipt))


def test_three_for_two_discount(teller: Teller, cart: ShoppingCart, toothbrush: Product) -> None:
    teller.add_special_offer(SpecialOfferType.THREE_FOR_TWO, toothbrush, 10.0)
    cart.add_item_quantity(toothbrush, 3)

    receipt = teller.checks_out_articles_from(cart)

    approvaltests.verify(ReceiptPrinter().print_receipt(receipt))


def test_three_for_two_discount_too_few(teller: Teller, cart: ShoppingCart, toothbrush: Product) -> None:
    teller.add_special_offer(SpecialOfferType.THREE_FOR_TWO, toothbrush, 10.0)
    cart.add_item_quantity(toothbrush, 2)

    receipt = teller.checks_out_articles_from(cart)

    approvaltests.verify(ReceiptPrinter().print_receipt(receipt))


def test_five_for_amount_discount(teller: Teller, cart: ShoppingCart, toothbrush: Product) -> None:
    teller.add_special_offer(SpecialOfferType.FIVE_FOR_AMOUNT, toothbrush, 4.0)
    cart.add_item_quantity(toothbrush, 5)

    receipt = teller.checks_out_articles_from(cart)

    approvaltests.verify(ReceiptPrinter().print_receipt(receipt))


def test_five_for_amount_discount_bought_too_few(teller: Teller, cart: ShoppingCart, toothbrush: Product) -> None:
    teller.add_special_offer(SpecialOfferType.FIVE_FOR_AMOUNT, toothbrush, 4.0)
    cart.add_item_quantity(toothbrush, 4)

    receipt = teller.checks_out_articles_from(cart)

    approvaltests.verify(ReceiptPrinter().print_receipt(receipt))


def test_two_for_amount_discount(teller: Teller, cart: ShoppingCart, toothbrush: Product) -> None:
    teller.add_special_offer(SpecialOfferType.TWO_FOR_AMOUNT, toothbrush, 1.80)
    cart.add_item_quantity(toothbrush, 5)

    receipt = teller.checks_out_articles_from(cart)

    approvaltests.verify(ReceiptPrinter().print_receipt(receipt))


def test_two_for_amount_discount_bought_too_few(teller: Teller, cart: ShoppingCart, toothbrush: Product):
    teller.add_special_offer(SpecialOfferType.TWO_FOR_AMOUNT, toothbrush, 1.80)
    cart.add_item_quantity(toothbrush, 1)

    receipt = teller.checks_out_articles_from(cart)

    approvaltests.verify(ReceiptPrinter().print_receipt(receipt))
