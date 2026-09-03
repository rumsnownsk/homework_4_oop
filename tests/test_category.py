from unittest.mock import patch

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_product():
    return Product("Хлеб", "Свежий", 50, 10)


@pytest.fixture(autouse=True)
def reset_category_count():
    """Сбрасываем счётчик категорий перед каждым тестом."""
    Category.category_count = 0
    yield


def test_category_init(category_1, category_2):
    assert isinstance(category_1, Category)
    assert isinstance(category_2, Category)

    assert category_1.name == "category_1"

    assert category_1.category_count == 2
    assert category_2.category_count == 2

    assert category_1.product_count == 2
    assert category_2.product_count == 3


def test_category_create_empty():
    cat = Category("Выпечка", "Всё про хлеб и булочки")
    assert cat.name == "Выпечка"
    assert cat.product_count == 0
    assert Category.category_count == 1


def test_category_create_with_products(sample_product):
    cat = Category("Выпечка", "Всё про хлеб", products=[sample_product])
    assert cat.product_count == 1
    assert Category.category_count == 1


@patch("builtins.print")
def test_add_product_success(mock_print, sample_product):
    cat = Category("Выпечка", "Описание")
    cat.add_product(sample_product)

    # Проверяем, что print был вызван ровно с таким текстом
    expected_msg = f"Новый продукт <{sample_product.name}> успешно добавлен для категории <{cat.name}> \n"
    mock_print.assert_called_once_with(expected_msg)

    assert cat.product_count == 1
    assert len(cat._Category__products) == 1  # доступ к приватному полю через имя-манглинг


def test_products_property_format(sample_product):
    cat = Category("Выпечка", "Описание", products=[sample_product])
    result = cat.products

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == f"{sample_product.name}, {sample_product.price} руб. Остаток: {sample_product.quantity} шт."


@patch("builtins.print")
def test_multiple_adds_and_counts(mock_print):
    p1 = Product("Хлеб", "Свежий", 50, 10)
    p2 = Product("Батон", "Нарезной", 60, 5)
    cat = Category("Выпечка", "Описание")

    cat.add_product(p1)
    cat.add_product(p2)

    assert cat.product_count == 2
    assert mock_print.call_count == 4  # print вызывался дважды

    products_list = cat.products
    assert len(products_list) == 2

    with pytest.raises(TypeError) as exc_info:
        Category("Выпечка", "Описание").add_product("не продукт")
    assert "Продукт должен быть экземпляром класса <Product>" in str(exc_info.value)
