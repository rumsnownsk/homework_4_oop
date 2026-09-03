from src.base_entity import BaseEntity
from src.product import Product


class Order(BaseEntity):
    def __init__(self, name, product: Product, quantity: int, description: str = ""):
        # строчкой super перетягиваем поля от Родителя
        super().__init__(name, description)

        # и добавляем ещё новые поля
        self.product = product
        self.quantity = quantity
        self._total_coast = self._calculate_total()

    def _calculate_total(self) -> int | float:
        return self.quantity * self.product.price

    def __str__(self):
        return f"<{self.name}>: {self.product.name}, {self.quantity} шт., на сумму {self._total_coast}"
