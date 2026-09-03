from src.print_mixin import PrintMixin
from typing import Dict, List

from src.base_product import BaseProduct


class Product(BaseProduct, PrintMixin):

    _list_products: list[Dict] = []

    def __init__(self, name, description, price: float | int = 0.0, quantity: int = 0):

        # Вызываем метод базового класса
        super().__init__(name, description, price, quantity)
        # self.name = name
        # self.description = description
        # self._price = price
        # self.quantity = quantity

        if not self._update_existing_product():
            self._add_new_product()

    def __str__(self):
        return f"{self.name}, {int(self._price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is type(other):
            return self._price * self.quantity + other._price * other.quantity
        else:
            raise TypeError("Складывать можно только товары одинаковой категории")

    def _update_existing_product(self) -> bool:
        for product in Product._list_products:
            if product["name"] == self.name:
                product["quantity"] += self.quantity
                return True
        return False

    def _add_new_product(self):
        Product._list_products.append(
            {"name": self.name, "description": self.description, "price": self._price, "quantity": self.quantity}
        )

    @classmethod
    def new_product(cls, data: dict):
        allowed = {"name", "description", "price", "quantity"}
        filtered = {k: v for k, v in data.items() if k in allowed}
        return cls(**filtered)

    @classmethod
    def all_products(cls) -> List[Dict]:
        return cls._list_products

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float | int) -> None:
        if not isinstance(value, (int, float)):
            print("Цена должна быть числом")
            return

        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self._price:
            print("Внимание! Новая цена ниже предыдущей! Снижаем цену товара? Подтвердите 'y' - да, 'n' - нет: \n")
            confirm = input("> ")

            if confirm.lower() == "y":
                self._price = float(value)  # <-- важно: пишем напрямую в _price
                self._sync_price_in_storage()
            else:
                print("Цена не должна быть ниже начальной стоимости товара")
        else:
            self._price = float(value)
            self._sync_price_in_storage()

    def _sync_price_in_storage(self) -> None:
        for prod_dict in Product._list_products:
            if prod_dict["name"] == self.name:
                prod_dict["price"] = self._price
                break
