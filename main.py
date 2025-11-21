# main.py (para fins de teste)
from singleton_catalog import client_code as singleton_demo
from builder_product import client_code as builder_demo
from proxy_product_access import client_code as proxy_demo
from visitor_pricing_rules import client_code as visitor_demo

def main():
    print("=== Padrão Singleton ===\n")
    singleton_demo()
    print("\n\n=== Padrão Builder ===\n")
    builder_demo()
    print("\n\n=== Padrão Proxy ===\n")
    proxy_demo()
    print("\n\n=== Padrão Visitor ===\n")
    visitor_demo()

if __name__ == "__main__":
    main()
