# main.py(OPCIONAL!!!!)
from singleton_guru import client_code as singleton_demo
from builder_guru import client_code as builder_demo
from proxy_guru import client_code as proxy_demo
from visitor_guru import client_code as visitor_demo

def main():
    print("=== DEMO: Singleton Pattern (Guru style) ===\n")
    singleton_demo()
    print("\n\n=== DEMO: Builder Pattern (Guru style) ===\n")
    builder_demo()
    print("\n\n=== DEMO: Proxy Pattern (Guru style) ===\n")
    proxy_demo()
    print("\n\n=== DEMO: Visitor Pattern (Guru style) ===\n")
    visitor_demo()

if __name__ == "__main__":
    main()
