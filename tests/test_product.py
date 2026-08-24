from src.product import Product


def test_product_init(one_product, two_product, three_product):
    assert isinstance(one_product, Product)
    assert isinstance(two_product, Product)

    assert one_product.name == "test_1"
    assert three_product.name == "test_3"
