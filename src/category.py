from src.product import Product


class Category:
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []

        # задаём кол-во Продуктов у атрибута экземпляра Category
        self.product_count = len(self.__products)

        # задаём кол-во Продуктов у атрибута класса Category
        Category.product_count += len(self.__products)

        # задаём общее кол-во Категорий
        Category.category_count += 1

    def add_product(self, new_product: Product):
        if not isinstance(new_product, Product):
            raise TypeError("Продукт должен быть экземпляром класса <Product>")

        if not new_product:
            raise ValueError("Ошибка. не передан новый продукт")
        self.__products.append(new_product)

        # если добавляем продукт в конкретную категорию то увеличиваем на 1 (единицу)
        self.product_count += 1

        # эта строчка добавляет 1(единицу) аж к единому неповторимому классу Category
        # в какое то волшебное невидимое внутреннее хранилище
        Category.product_count += 1

        print(f"Новый продукт <{new_product.name}> успешно добавлен для категории <{self.name}> \n")

    @property
    def products(self):
        return [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products]

    def __str__(self):
        count_products_by_category = sum([item.quantity for item in self.__products])
        return f"{self.name}, количество продуктов: {count_products_by_category} шт."
