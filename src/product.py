class Product:
    name: str
    description: str
    price: float | int
    quantity: int

    def __init__(self, name, description, price: float | int = 0.0, quantity: int = 0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
