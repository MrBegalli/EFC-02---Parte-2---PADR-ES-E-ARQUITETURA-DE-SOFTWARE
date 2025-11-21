# builder_product.py
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict


class AbstractProduct(ABC):
    """
    Interface de Produto para um item da Loja Virtual.
    """

    @abstractmethod
    def product_info(self) -> str:
        pass


class ConcreteProduct1(AbstractProduct):
    def __init__(self, parts: Dict):
        self.parts = parts

    def product_info(self) -> str:
        return f"PhysicalProduct (parts={self.parts})"


class ConcreteProduct2(AbstractProduct):
    def __init__(self, parts: Dict):
        self.parts = parts

    def product_info(self) -> str:
        return f"DigitalProduct (parts={self.parts})"


class AbstractBuilder(ABC):
    """
    A interface Builder declara as etapas de construção do produto.
    """

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def set_name(self, name: str) -> None:
        pass

    @abstractmethod
    def set_price(self, price: float) -> None:
        pass

    @abstractmethod
    def set_metadata(self, key: str, value) -> None:
        pass

    @abstractmethod
    def build(self) -> AbstractProduct:
        pass


class ConcreteBuilder1(AbstractBuilder):
    """
    Builder para ConcreteProduct1 (ex: um produto físico).
    """

    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._parts = {"type": "physical", "name": None, "price": 0.0, "meta": {}}

    def set_name(self, name: str) -> None:
        self._parts["name"] = name

    def set_price(self, price: float) -> None:
        self._parts["price"] = price

    def set_metadata(self, key: str, value) -> None:
        self._parts["meta"][key] = value

    def build(self) -> ConcreteProduct1:
        product = ConcreteProduct1(parts=self._parts.copy())
        self.reset()
        return product


class ConcreteBuilder2(AbstractBuilder):
    """
    Builder para ConcreteProduct2 (ex: um produto digital).
    """

    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._parts = {"type": "digital", "name": None, "price": 0.0, "meta": {}}

    def set_name(self, name: str) -> None:
        self._parts["name"] = name

    def set_price(self, price: float) -> None:
        self._parts["price"] = price

    def set_metadata(self, key: str, value) -> None:
        self._parts["meta"][key] = value

    def build(self) -> ConcreteProduct2:
        product = ConcreteProduct2(parts=self._parts.copy())
        self.reset()
        return product


def client_code() -> None:
    """
    O código cliente pode trabalhar com qualquer builder através da interface AbstractBuilder.
    """
    print("Cliente: Testando Builder com ConcreteBuilder1 (físico):")
    builder1 = ConcreteBuilder1()
    builder1.set_name("Camiseta Polo")
    builder1.set_price(79.9)
    builder1.set_metadata("color", "azul")
    product1 = builder1.build()
    print(product1.product_info())

    print("\nCliente: Testando Builder com ConcreteBuilder2 (digital):")
    builder2 = ConcreteBuilder2()
    builder2.set_name("Curso Python")
    builder2.set_price(199.9)
    builder2.set_metadata("duration", "10h")
    product2 = builder2.build()
    print(product2.product_info())


if __name__ == "__main__":
    client_code()