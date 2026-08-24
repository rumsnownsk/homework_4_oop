import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def one_product():
    return Product(
        name="test_1",
        description="test_description_1",
        price=100.0,
        quantity=10
    )

@pytest.fixture
def two_product():
    return Product(
        name="test_2",
        description="test_description_2",
        price=200.0,
        quantity=20
    )

@pytest.fixture
def three_product():
    return Product(
        name="test_3",
        description="test_description_3",
        price=300.0,
        quantity=30
    )

@pytest.fixture
def category_1():
    return Category(
        name="category_1",
        description="description_for_category_1",
        products=[
            Product("Картофель", "свежий мытый", 100.0, 10),
            Product("Яблоко", "жёлтый сладкий", 150.0, 100)
        ]
    )

@pytest.fixture
def category_2():
    return Category(
        name="category_2",
        description="description_for_category_2",
        products=[
            Product("помидор", "сочный спелый овощ", 50.0, 10),
            Product("редис", "горкий мелкий корнеплод", 20.0, 100),
            Product("редис мытый", "", 20.0, 100)
        ]
    )