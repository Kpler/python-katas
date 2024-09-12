import pytest

from tests.fake_catalog import FakeCatalog
from src.model_objects import Product, ProductUnit
from src.shopping_cart import ShoppingCart
from src.teller import Teller


@pytest.fixture
def toothbrush() -> Product:
    return Product("toothbrush", ProductUnit.EACH)


@pytest.fixture
def apples() -> Product:
    return Product("apples", ProductUnit.KILO)


@pytest.fixture
def catalog(toothbrush: Product, apples: Product) -> FakeCatalog:
    catalog = FakeCatalog()
    catalog.add_product(toothbrush, 0.99)
    catalog.add_product(apples, 1.99)
    return catalog


@pytest.fixture
def teller(catalog: FakeCatalog) -> Teller:
    return Teller(catalog)


@pytest.fixture
def cart():
    return ShoppingCart()
