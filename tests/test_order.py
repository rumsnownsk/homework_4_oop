from src.order import Order
from src.product import Product


def test_order_creation_and_total_cost():
    product = Product("Ноутбук", "Описание", 50000, 3)
    order = Order("Заказ №1", product, 2)
    assert order.name == "Заказ №1"
    assert order.product is product
    assert order.quantity == 2
    assert order._total_coast == 100000  # 50000 * 2d
