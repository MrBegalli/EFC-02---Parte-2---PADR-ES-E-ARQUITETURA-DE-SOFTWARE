# visitor_pricing_rules.py
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Protocol, List, Dict


class AbstractElement(ABC):
    """
    AbstractElement para o padrão Visitor na Loja Virtual (products).
    """

    @abstractmethod
    def accept(self, visitor: "AbstractVisitor") -> Any:
        pass


class ProductElement(AbstractElement):
    """
    ProductElement com atributos básicos que serão visitados.
    """

    def __init__(self, sku: str, name: str, price: float, tags: List[str] = None, metadata: Dict = None):
        self.sku = sku
        self.name = name
        self.price = price
        self.tags = tags or []
        self.metadata = metadata or {}

    def accept(self, visitor: "AbstractVisitor") -> Any:
        return visitor.visit_product(self)


class AbstractVisitor(ABC):
    """
    Interface Visitor declara operações de visitas para ProductElements.
    """

    @abstractmethod
    def visit_product(self, product: ProductElement) -> Any:
        pass


class ConcreteVisitor1(AbstractVisitor):
    """
    Pricing Visitor variante 1: desconto simples de porcentagem a partir da chave metadata 'discount_pct'.
    """

    def visit_product(self, product: ProductElement) -> float:
        price = float(product.price)
        discount = product.metadata.get("discount_pct", 0)
        if discount:
            price = price * (1 - discount / 100.0)
        return round(price, 2)


class ConcreteVisitor2(AbstractVisitor):
    """
    Pricing Visitor variante 2: aplica regras com base em tag (tag-based) (ex: 'clearance' divide o preço pela metade).
    """

    def visit_product(self, product: ProductElement) -> float:
        price = float(product.price)
        if "clearance" in product.tags:
            price = price * 0.5
        discount = product.metadata.get("discount_pct", 0)
        if discount:
            price = price * (1 - discount / 100.0)
        return round(price, 2)


def client_code() -> None:
    """
    Demonstra ProductElements para 2 diferentes visitantes.
    """
    p1 = ProductElement("SKU-001", "Camiseta Polo", 79.9, tags=["clothing"], metadata={})
    p2 = ProductElement("SKU-004", "Relógio Promo", 129.9, tags=["clearance"], metadata={"discount_pct": 10})

    print("Cliente: usando ConcreteVisitor1 (desconto):")
    v1 = ConcreteVisitor1()
    print(f"{p1.name}: R$ {p1.accept(v1)}")
    print(f"{p2.name}: R$ {p2.accept(v1)}")  # 10% de desconto

    print("\nClient: Using ConcreteVisitor2 (tag rules):")
    v2 = ConcreteVisitor2()
    print(f"{p1.name}: R$ {p1.accept(v2)}")
    print(f"{p2.name}: R$ {p2.accept(v2)}")
