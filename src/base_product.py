from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        super().__init__()

    @abstractmethod
    def new_product(self, *args, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def all_products(cls):
        pass
