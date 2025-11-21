# proxy_product_access.py
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Optional
import time


class AbstractSubject(ABC):
    """
    A interface Subject declara operações comuns para RealSubject e Proxy.
    Na Loja Virtual, representa a recuperação do produto.
    """

    @abstractmethod
    def get_product(self, sku: str) -> Optional[Dict]:
        pass


class RealSubject1(AbstractSubject):
    """
    Variante 1 do RealSubject: Simula a loja de produtos A (ex: físico).
    """

    def __init__(self):
        # simula um DB/store
        self._store = {
            "SKU-001": {"sku": "SKU-001", "name": "Camiseta Polo", "price": 79.9},
            "SKU-002": {"sku": "SKU-002", "name": "Tênis Runner", "price": 349.9},
        }

    def get_product(self, sku: str) -> Optional[Dict]:
        # simula latência
        time.sleep(0.02)
        print(f"[RealSubject1] buscando {sku} da loja A")
        return self._store.get(sku)


class RealSubject2(AbstractSubject):
    """
    Variante 2 do RealSubject: Simula a loja de produtos B (ex: digital).
    """

    def __init__(self):
        self._store = {
            "SKU-003": {"sku": "SKU-003", "name": "Curso Python", "price": 199.9},
            "SKU-004": {"sku": "SKU-004", "name": "Ebook", "price": 29.9},
        }

    def get_product(self, sku: str) -> Optional[Dict]:
        time.sleep(0.02)
        print(f"[RealSubject2] buscando {sku} da loja B")
        return self._store.get(sku)


class Proxy1(AbstractSubject):
    """
    Variante 1 do Proxy: adiciona cache simples e controle sem autenticação para RealSubject1.
    """

    def __init__(self, real_subject: RealSubject1):
        self._real = real_subject
        self._cache: Dict[str, Dict] = {}

    def get_product(self, sku: str) -> Optional[Dict]:
        if sku in self._cache:
            print(f"[Proxy1] Cache hit para {sku}")
            return self._cache[sku]
        print(f"[Proxy1] Cache miss para {sku} - chamando RealSubject1")
        p = self._real.get_product(sku)
        if p:
            self._cache[sku] = p
        return p


class Proxy2(AbstractSubject):
    """
    Variante 2 do Proxy: adiciona proteção simples por token e cache para RealSubject2.
    """

    def __init__(self, real_subject: RealSubject2, token: str = "valid-token"):
        self._real = real_subject
        self._cache: Dict[str, Dict] = {}
        self._token = token

    def _check_token(self, token: str):
        if token != self._token:
            raise PermissionError("Token inválido para Proxy2")

    def get_product(self, sku: str, token: str = "") -> Optional[Dict]:
        # nota: a assinatura difere para aceitar o token: esta é uma variante didática
        self._check_token(token)
        if sku in self._cache:
            print(f"[Proxy2] Cache hit para {sku}")
            return self._cache[sku]
        print(f"[Proxy2] Cache miss para {sku} - chamando RealSubject2")
        p = self._real.get_product(sku)
        if p:
            self._cache[sku] = p
        return p


def client_code() -> None:
    """
    Demonstra o uso de RealSubject + Proxy.
    """
    print("Cliente: Testando Proxy1 com RealSubject1:")
    real1 = RealSubject1()
    proxy1 = Proxy1(real1)
    print(proxy1.get_product("SKU-001"))
    print(proxy1.get_product("SKU-001"))  # deve ser cache hit

    print("\nCliente: Testando Proxy2 com RealSubject2 (requer token):")
    real2 = RealSubject2()
    proxy2 = Proxy2(real2, token="valid-token")
    # chamada com token válido
    print(proxy2.get_product("SKU-003", token="valid-token"))
    try:
        # chamada com token inválido para mostrar a proteção
        print(proxy2.get_product("SKU-004", token="bad-token"))
    except PermissionError as e:
        print("[Proxy2] PermissionError capturado:", e)


if __name__ == "__main__":
    client_code()