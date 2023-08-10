from __future__ import annotations
from abc import ABC


class Mediador(ABC):
    """
    La interfaz Mediador declara un método utilizado por los componentes para notificar al
    mediador sobre diversos eventos. El Mediador puede reaccionar a estos eventos y
    pasar la ejecución a otros componentes.
    """

    def notificar(self, remitente: object, evento: str) -> None:
        pass


class MediadorConcreto(Mediador):
    def __init__(self, componente1: Componente1, componente2: Componente2) -> None:
        self._componente1 = componente1
        self._componente1.mediador = self
        self._componente2 = componente2
        self._componente2.mediador = self

    def notificar(self, remitente: object, evento: str) -> None:
        if evento == "A":
            print("El mediador reacciona a A y activa las siguientes operaciones:")
            self._componente2.hacer_c()
        elif evento == "D":
            print("El mediador reacciona a D y activa las siguientes operaciones:")
            self._componente1.hacer_b()
            self._componente2.hacer_c()


class ComponenteBase:
    """
    El Componente Base proporciona la funcionalidad básica de almacenar una instancia de
    mediador dentro de los objetos de componente.
    """

    def __init__(self, mediador: Mediador = None) -> None:
        self._mediador = mediador

    @property
    def mediador(self) -> Mediador:
        return self._mediador

    @mediador.setter
    def mediador(self, mediador: Mediador) -> None:
        self._mediador = mediador


"""
Los Componentes Concretos implementan diversas funcionalidades. No dependen de otros
componentes. Tampoco dependen de ninguna clase mediadora concreta.
"""


class Componente1(ComponenteBase):
    def hacer_a(self) -> None:
        print("Componente 1 hace A.")
        self.mediador.notificar(self, "A")

    def hacer_b(self) -> None:
        print("Componente 1 hace B.")
        self.mediador.notificar(self, "B")


class Componente2(ComponenteBase):
    def hacer_c(self) -> None:
        print("Componente 2 hace C.")
        self.mediador.notificar(self, "C")

    def hacer_d(self) -> None:
        print("Componente 2 hace D.")
        self.mediador.notificar(self, "D")


if __name__ == "__main__":
    # El código del cliente.
    c1 = Componente1()
    c2 = Componente2()
    mediador = MediadorConcreto(c1, c2)

    print("El cliente activa la operación A.")
    c1.hacer_a()

    print("\n", end="")

    print("El cliente activa la operación D.")
    c2.hacer_d()
