import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def one_product():
    return Product(name="test_1", description="test_description_1", price=100.0, quantity=10)


@pytest.fixture
def two_product():
    return Product(name="test_2", description="test_description_2", price=200.0, quantity=20)


@pytest.fixture
def three_product():
    return Product(name="test_3", description="test_description_3", price=300.0, quantity=30)


@pytest.fixture
def category_1():
    return Category(
        name="category_1",
        description="description_for_category_1",
        products=[Product("Картофель", "свежий мытый", 100.0, 10), Product("Яблоко", "жёлтый сладкий", 150.0, 100)],
    )


@pytest.fixture
def category_2():
    return Category(
        name="category_2",
        description="description_for_category_2",
        products=[
            Product("помидор", "сочный спелый овощ", 50.0, 10),
            Product("редис", "горкий мелкий корнеплод", 20.0, 100),
            Product("редис мытый", "", 20.0, 100),
        ],
    )

@pytest.fixture()
def smartphone_1():
    return Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый"
    )

@pytest.fixture()
def smartphone_2():
    return Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый"
    )

@pytest.fixture()
def grass_1():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )
