from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Sujeto(ABC):
    """
    La interfaz Sujeto declara un conjunto de métodos para gestionar los suscriptores.
    """

    @abstractmethod
    def adjuntar(self, observador: Observador) -> None:
        """
        Adjuntar un observador al sujeto.
        """
        pass

    @abstractmethod
    def desadjuntar(self, observador: Observador) -> None:
        """
        Desadjuntar un observador del sujeto.
        """
        pass

    @abstractmethod
    def notificar(self) -> None:
        """
        Notificar a todos los observadores sobre un evento.
        """
        pass


class SujetoConcreto(Sujeto):
    """
    El Sujeto posee un estado importante y notifica a los observadores cuando el estado cambia.
    """

    _estado: int = None
    """
    Por simplicidad, el estado del Sujeto, esencial para todos los suscriptores, se almacena en esta variable.
    """

    _observadores: List[Observador] = []
    """
    Lista de suscriptores. En la vida real, la lista de suscriptores se puede almacenar de manera más completa (categorizada por tipo de evento, etc.).
    """

    def adjuntar(self, observador: Observador) -> None:
        print("Sujeto: Se adjuntó un observador.")
        self._observadores.append(observador)

    def desadjuntar(self, observador: Observador) -> None:
        self._observadores.remove(observador)

    """
    Métodos de gestión de suscripción.
    """

    def notificar(self) -> None:
        """
        Desencadenar una actualización en cada suscriptor.
        """

        print("Sujeto: Notificando a los observadores...")
        for observador in self._observadores:
            observador.actualizar(self)

    def logica_de_negocio(self) -> None:
        """
        Por lo general, la lógica de suscripción es solo una parte de lo que un Sujeto realmente puede hacer.
        Los Sujetos comúnmente tienen alguna lógica de negocio importante que
        activa un método de notificación cada vez que algo importante está a punto de
        suceder (o después).
        """

        print("\nSujeto: Estoy haciendo algo importante.")
        self._estado = randrange(0, 10)

        print(f"Sujeto: Mi estado acaba de cambiar a: {self._estado}")
        self.notificar()


class Observador(ABC):
    """
    La interfaz Observador declara el método actualizar, utilizado por los sujetos.
    """

    @abstractmethod
    def actualizar(self, sujeto: Sujeto) -> None:
        """
        Recibir actualización del sujeto.
        """
        pass


"""
Los Observadores Concretos reaccionan a las actualizaciones emitidas por el Sujeto al que estaban adjuntos.
"""


class ObservadorConcretoA(Observador):
    def actualizar(self, sujeto: Sujeto) -> None:
        if sujeto._estado < 3:
            print("ObservadorConcretoA: Reaccionó al evento")


class ObservadorConcretoB(Observador):
    def actualizar(self, sujeto: Sujeto) -> None:
        if sujeto._estado == 0 or sujeto._estado >= 2:
            print("ObservadorConcretoB: Reaccionó al evento")


if __name__ == "__main__":
    # El código del cliente.

    sujeto = SujetoConcreto()

    observador_a = ObservadorConcretoA()
    sujeto.adjuntar(observador_a)

    observador_b = ObservadorConcretoB()
    sujeto.adjuntar(observador_b)

    sujeto.logica_de_negocio()
    sujeto.logica_de_negocio()

    sujeto.desadjuntar(observador_a)

    sujeto.logica_de_negocio()
