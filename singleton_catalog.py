# singleton_catalog.py
from __future__ import annotations
from abc import ABC, abstractmethod
import threading

class AbstractSingleton(ABC):
    """
    Exemplo de 'AbstractSingleton' (didático): declara uma interface para um
    serviço tipo singleton no contexto da Loja Virtual.
    """

    @abstractmethod
    def connection_info(self) -> str:
        pass


class ConcreteSingleton1(AbstractSingleton):
    """
    Variante 1 do singleton concreto: InMemoryCatalogSingleton.
    Implementa um singleton thread-safe: apenas uma instância por classe.
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
        # store simula o armazenamento do catálogo
        self._store = {"variant": "PhysicalCatalogV1", "products": []}

    def connection_info(self) -> str:
        return f"InMemoryCatalogSingleton V1 — variant={self._store['variant']}"


class ConcreteSingleton2(AbstractSingleton):
    """
    Variante 2 do singleton concreto: InMemoryCatalogSingleton com um 'variant' diferente
    para demonstrar duas variantes de singleton no estilo Guru.
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
    O código cliente trabalha com singletons através do tipo abstrato.
    Demonstra que múltiplas chamadas resultam na mesma instância por classe concreta.
    """
    print("Cliente: Testando o comportamento do singleton com ConcreteSingleton1:")
    s1_a = ConcreteSingleton1()
    s1_b = ConcreteSingleton1()
    print(s1_a.connection_info())
    print("Mesma instância?" , s1_a is s1_b)

    print("\nCliente: Testando o comportamento do singleton com ConcreteSingleton2:")
    s2_a = ConcreteSingleton2()
    s2_b = ConcreteSingleton2()
    print(s2_a.connection_info())
    print("Mesma instância?" , s2_a is s2_b)


if __name__ == "__main__":
    client_code()