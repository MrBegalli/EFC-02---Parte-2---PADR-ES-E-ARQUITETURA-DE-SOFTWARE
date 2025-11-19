# proxy_guru.py
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Optional
import time


class AbstractSubject(ABC):
    """
    The Subject interface declares common operations for RealSubject and Proxy.
    In Loja Virtual it represents product retrieval.
    """

    @abstractmethod
    def get_product(self, sku: str) -> Optional[Dict]:
        pass


class RealSubject1(AbstractSubject):
    """
    RealSubject variant 1: Simulates product store A (e.g., physical).
    """

    def __init__(self):
        # simulate a DB/store
        self._store = {
            "SKU-001": {"sku": "SKU-001", "name": "Camiseta Polo", "price": 79.9},
            "SKU-002": {"sku": "SKU-002", "name": "Tênis Runner", "price": 349.9},
        }

    def get_product(self, sku: str) -> Optional[Dict]:
        # simulate latency
        time.sleep(0.02)
        print(f"[RealSubject1] fetching {sku} from store A")
        return self._store.get(sku)


class RealSubject2(AbstractSubject):
    """
    RealSubject variant 2: Simulates product store B (e.g., digital).
    """

    def __init__(self):
        self._store = {
            "SKU-003": {"sku": "SKU-003", "name": "Curso Python", "price": 199.9},
            "SKU-004": {"sku": "SKU-004", "name": "Ebook", "price": 29.9},
        }

    def get_product(self, sku: str) -> Optional[Dict]:
        time.sleep(0.02)
        print(f"[RealSubject2] fetching {sku} from store B")
        return self._store.get(sku)


class Proxy1(AbstractSubject):
    """
    Proxy variant 1: adds simple cache and no-auth control for RealSubject1.
    """

    def __init__(self, real_subject: RealSubject1):
        self._real = real_subject
        self._cache: Dict[str, Dict] = {}

    def get_product(self, sku: str) -> Optional[Dict]:
        if sku in self._cache:
            print(f"[Proxy1] Cache hit for {sku}")
            return self._cache[sku]
        print(f"[Proxy1] Cache miss for {sku} - calling RealSubject1")
        p = self._real.get_product(sku)
        if p:
            self._cache[sku] = p
        return p


class Proxy2(AbstractSubject):
    """
    Proxy variant 2: adds simple token protection and caching for RealSubject2.
    """

    def __init__(self, real_subject: RealSubject2, token: str = "valid-token"):
        self._real = real_subject
        self._cache: Dict[str, Dict] = {}
        self._token = token

    def _check_token(self, token: str):
        if token != self._token:
            raise PermissionError("Invalid token for Proxy2")

    def get_product(self, sku: str, token: str = "") -> Optional[Dict]:
        # note: signature differs to accept token — this is a didactic variant
        self._check_token(token)
        if sku in self._cache:
            print(f"[Proxy2] Cache hit for {sku}")
            return self._cache[sku]
        print(f"[Proxy2] Cache miss for {sku} - calling RealSubject2")
        p = self._real.get_product(sku)
        if p:
            self._cache[sku] = p
        return p


def client_code() -> None:
    """
    Demonstrates using RealSubject + Proxy.
    """
    print("Client: Testing Proxy1 with RealSubject1:")
    real1 = RealSubject1()
    proxy1 = Proxy1(real1)
    print(proxy1.get_product("SKU-001"))
    print(proxy1.get_product("SKU-001"))  # should be cache hit

    print("\nClient: Testing Proxy2 with RealSubject2 (requires token):")
    real2 = RealSubject2()
    proxy2 = Proxy2(real2, token="valid-token")
    # call with valid token
    print(proxy2.get_product("SKU-003", token="valid-token"))
    try:
        # call with invalid token to show protection
        print(proxy2.get_product("SKU-004", token="bad-token"))
    except PermissionError as e:
        print("[Proxy2] PermissionError caught:", e)


if __name__ == "__main__":
    client_code()
