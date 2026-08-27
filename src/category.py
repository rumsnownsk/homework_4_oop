from src.product import Product


class Category:
    category_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        self.product_count = len(self.__products)

    def add_product(self, new_product: Product):
        if not new_product:
            raise ValueError("Ошибка. не передан новый продукт")
        self.__products.append(new_product)
        self.product_count += 1
        print(f"Новый продукт <{new_product.name}> успешно добавлен для категории <{self.name}> \n")

    @property
    def products(self):
        return [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products]
