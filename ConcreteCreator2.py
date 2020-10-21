from ConcreteProduct2 import ConcreteProduct2
from Creator import Creator
from Product import Product


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()
