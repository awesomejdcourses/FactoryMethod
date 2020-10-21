from __future__ import annotations

from ConcreteCreator1 import ConcreteCreator1
from ConcreteCreator2 import ConcreteCreator2
from Creator import Creator


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, though through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())