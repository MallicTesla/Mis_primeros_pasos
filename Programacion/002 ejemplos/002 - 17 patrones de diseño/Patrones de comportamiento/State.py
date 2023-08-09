from __future__ import annotations
from abc import ABC, abstractmethod


class Contexto:
    """
    El Contexto define la interfaz de interés para los clientes. También mantiene
    una referencia a una instancia de una subclase Estado, que representa el estado
    actual del Contexto.
    """

    _estado = None
    """
    Una referencia al estado actual del Contexto.
    """

    def __init__(self, estado: Estado) -> None:
        self.transicionar_a(estado)

    def transicionar_a(self, estado: Estado):
        """
        El Contexto permite cambiar el objeto Estado en tiempo de ejecución.
        """

        print(f"Contexto: Transición a {type(estado).__name__}")
        self._estado = estado
        self._estado.contexto = self

    """
    El Contexto delega parte de su comportamiento al objeto Estado actual.
    """

    def solicitud1(self):
        self._estado.manipular1()

    def solicitud2(self):
        self._estado.manipular2()


class Estado(ABC):
    """
    La clase base Estado declara los métodos que todos los Estados Concretos deben
    implementar y también proporciona una referencia inversa al objeto Contexto,
    asociado con el Estado. Esta referencia inversa puede ser usada por los Estados
    para hacer transiciones en el Contexto a otro Estado.
    """

    @property
    def contexto(self) -> Contexto:
        return self._contexto

    @contexto.setter
    def contexto(self, contexto: Contexto) -> None:
        self._contexto = contexto

    @abstractmethod
    def manipular1(self) -> None:
        pass

    @abstractmethod
    def manipular2(self) -> None:
        pass


"""
Los Estados Concretos implementan varios comportamientos, asociados con un estado
del Contexto.
"""


class EstadoConcretoA(Estado):
    def manipular1(self) -> None:
        print("EstadoConcretoA maneja solicitud1.")
        print("EstadoConcretoA quiere cambiar el estado del contexto.")
        self.contexto.transicionar_a(EstadoConcretoB())

    def manipular2(self) -> None:
        print("EstadoConcretoA maneja solicitud2.")


class EstadoConcretoB(Estado):
    def manipular1(self) -> None:
        print("EstadoConcretoB maneja solicitud1.")

    def manipular2(self) -> None:
        print("EstadoConcretoB maneja solicitud2.")
        print("EstadoConcretoB quiere cambiar el estado del contexto.")
        self.contexto.transicionar_a(EstadoConcretoA())


if __name__ == "__main__":
    # El código del cliente.

    contexto = Contexto(EstadoConcretoA())
    contexto.solicitud1()
    contexto.solicitud2()
