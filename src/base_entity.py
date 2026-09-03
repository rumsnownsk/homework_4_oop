from abc import ABC, abstractmethod


class BaseEntity(ABC):
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self) -> str:
        pass
