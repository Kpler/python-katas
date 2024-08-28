import pytest

from supermarket_receipt.src.model_objects import Product, SpecialOfferType, ProductUnit
from supermarket_receipt.src.shopping_cart import ShoppingCart
from supermarket_receipt.src.teller import Teller
from supermarket_receipt.tests.fake_catalog import FakeCatalog


def test_ten_percent_discount():
    catalog = FakeCatalog()
    teller = Teller(catalog)
    cart = ShoppingCart()

    toothbrush = Product("toothbrush", ProductUnit.EACH)
    apples = Product("apples", ProductUnit.KILO)

    catalog.add_product(toothbrush, 0.99)
    catalog.add_product(apples, 1.99)
    teller.add_special_offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, toothbrush, 10.0)

    cart.add_item_quantity(apples, 2.5)
    receipt = teller.checks_out_articles_from(cart)

    assert 4.975 == pytest.approx(receipt.total_price(), 0.01)
    assert [] == receipt.discounts
    assert 1 == len(receipt.items)
    receipt_item = receipt.items[0]
    assert apples == receipt_item.product
    assert 1.99 == receipt_item.price
    assert 2.5 * 1.99 == pytest.approx(receipt_item.total_price, 0.01)
    assert 2.5 == receipt_item.quantity

def test_explore():
    catalog = FakeCatalog()
    teller = Teller(catalog)
    cart = ShoppingCart()

    # things to catalog
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    toothpaste = Product("toothpaste", ProductUnit.EACH)
    apples = Product("apples", ProductUnit.KILO)

    catalog.add_product(toothbrush, 1)
    catalog.add_product(toothpaste, 3)

    teller.add_bundle_discount([toothbrush, toothpaste], 10)

    # things to cart
    cart.add_item_quantity(toothbrush, 1)
    cart.add_item_quantity(toothpaste, 1)
    receipt = teller.checks_out_articles_from(cart)
    assert 3.6 == pytest.approx(receipt.total_price(), 0.01)



def test_explore_2():
    catalog = FakeCatalog()
    teller = Teller(catalog)
    cart = ShoppingCart()

    # things to catalog
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    toothpaste = Product("toothpaste", ProductUnit.EACH)
    apples = Product("apples", ProductUnit.KILO)

    catalog.add_product(toothbrush, 1)
    catalog.add_product(toothpaste, 3)

    teller.add_bundle_discount([toothbrush, toothpaste], 10)

    # things to cart
    cart.add_item_quantity(toothbrush, 2)
    cart.add_item_quantity(toothpaste, 2)
    receipt = teller.checks_out_articles_from(cart)
    assert 7.2 == pytest.approx(receipt.total_price(), 0.01)


def test_explore_3():
    catalog = FakeCatalog()
    teller = Teller(catalog)
    cart = ShoppingCart()

    # things to catalog
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    toothpaste = Product("toothpaste", ProductUnit.EACH)
    apples = Product("apples", ProductUnit.KILO)

    catalog.add_product(toothbrush, 1)
    catalog.add_product(toothpaste, 3)

    teller.add_bundle_discount([toothbrush, toothpaste], 10)

    # things to cart
    cart.add_item_quantity(toothbrush, 1) # total: 1 -> - 10 -> 0.9
    cart.add_item_quantity(toothpaste, 2) # total: 6 -> - 10 on 1 -> 3 + 2.7 = 5.7
    receipt = teller.checks_out_articles_from(cart)
    assert 6.6 == pytest.approx(receipt.total_price(), 0.01)

