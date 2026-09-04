class PrintMixin:

    def __init__(self, *args, **kwargs):
        print(repr(self))
        super().__init__(*args, **kwargs)

    # Для вывода информации переопределяем магический метод
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self._price}, {self.quantity})"
