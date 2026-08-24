from src.category import Category


def test_category_init(category_1, category_2):
    assert isinstance(category_1, Category)
    assert isinstance(category_2, Category)

    assert category_1.name == "category_1"

    assert category_1.category_count == 2
    assert category_2.category_count == 2

    assert category_1.product_count == 3
    assert category_2.product_count == 3