from unittest.mock import patch

import pytest

from src.product import Product


@pytest.fixture(autouse=True)
def reset_storage():
    """Сбрасываем хранилище перед каждым тестом, чтобы тесты не влияли друг на друга."""
    Product._list_products = []
    yield


def test_product_init(one_product, two_product, three_product):
    assert isinstance(one_product, Product)
    assert isinstance(two_product, Product)

    assert one_product.name == "test_1"
    assert three_product.name == "test_3"


def test_create_product():
    p = Product("Хлеб", "Свежий", 50, 10)
    assert p.name == "Хлеб"
    assert p.price == 50.0
    assert p.quantity == 10


def test_new_product_filters_extra_fields():
    data = {
        "name": "Молоко",
        "description": "Пастеризованное",
        "price": 80,
        "quantity": 5,
        "extra_field": "лишнее",
    }
    p = Product.new_product(data)
    assert p.name == "Молоко"
    assert "extra_field" not in p.__dict__


@patch("builtins.input", return_value="y")
@patch("builtins.print")
def test_price_setter_decrease_confirmed(mock_print, mock_input):
    p = Product("Товар", "Описание", 100)
    p.price = 50  # цена ниже — должен спросить и принять

    # Проверяем, что спросили
    mock_print.assert_any_call(
        "Внимание! Новая цена ниже предыдущей! Снижаем цену товара? Подтвердите 'y' - да, 'n' - нет: \n"
    )

    assert p.price == 50.0


@patch("builtins.input", return_value="n")
@patch("builtins.print")
def test_price_setter_decrease_rejected(mock_print, mock_input):
    p = Product("Товар", "Описание", 100)
    p.price = 50

    mock_print.assert_any_call(
        "Внимание! Новая цена ниже предыдущей! Снижаем цену товара? Подтвердите 'y' - да, 'n' - нет: \n"
    )
    mock_print.assert_any_call("Цена не должна быть ниже начальной стоимости товара")

    # Цена НЕ должна измениться
    assert p.price == 100.0


def test_price_setter_type_error_prints_message():
    p = Product("Товар", "Описание", 100)
    with patch("builtins.print") as mock_print:
        p.price = "не число"
        mock_print.assert_called_once_with("Цена должна быть числом")


@patch("builtins.print")
def test_price_setter_increase_works_without_input(mock_print):
    p = Product("Товар", "Описание", 100)
    p.price = 150
    # print не должен вызываться для случая увеличения
    mock_print.assert_not_called()
    assert p.price == 150.0


def test_storage_sync_on_price_change():
    Product._list_products = []
    p = Product("Хлеб", "Свежий", 50, 10)

    stored = Product.all_products()
    assert stored[0]["price"] == 50.0

    p.price = 60
    stored = Product.all_products()
    assert stored[0]["price"] == 60.0
