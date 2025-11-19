# singleton_guru.py
from __future__ import annotations
from abc import ABC, abstractmethod
import threading

class AbstractSingleton(ABC):
    """
    Example-style 'AbstractSingleton' (didactic): declares an interface for a
    singleton-like service in the Loja Virtual context.
    """

    @abstractmethod
    def connection_info(self) -> str:
        pass


class ConcreteSingleton1(AbstractSingleton):
    """
    Concrete singleton variant 1: InMemoryCatalogSingleton.
    Implements a thread-safe singleton: only one instance per class.
    """

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(ConcreteSingleton1, cls).__new__(cls)
                    cls._instance._init_store()
        return cls._instance

    def _init_store(self):
        # store simulates catalog storage
        self._store = {"variant": "PhysicalCatalogV1", "products": []}

    def connection_info(self) -> str:
        return f"InMemoryCatalogSingleton V1 — variant={self._store['variant']}"


class ConcreteSingleton2(AbstractSingleton):
    """
    Concrete singleton variant 2: InMemoryCatalogSingleton with a different 'variant'
    to demonstrate two singleton variants in Guru style.
    """

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(ConcreteSingleton2, cls).__new__(cls)
                    cls._instance._init_store()
        return cls._instance

    def _init_store(self):
        self._store = {"variant": "DigitalCatalogV2", "products": []}

    def connection_info(self) -> str:
        return f"InMemoryCatalogSingleton V2 — variant={self._store['variant']}"


def client_code() -> None:
    """
    The client code works with singletons through the abstract type.
    Demonstrates that multiple calls yield the same instance per concrete class.
    """
    print("Client: Testing singleton behavior with ConcreteSingleton1:")
    s1_a = ConcreteSingleton1()
    s1_b = ConcreteSingleton1()
    print(s1_a.connection_info())
    print("Same instance?" , s1_a is s1_b)

    print("\nClient: Testing singleton behavior with ConcreteSingleton2:")
    s2_a = ConcreteSingleton2()
    s2_b = ConcreteSingleton2()
    print(s2_a.connection_info())
    print("Same instance?" , s2_a is s2_b)


if __name__ == "__main__":
    client_code()
