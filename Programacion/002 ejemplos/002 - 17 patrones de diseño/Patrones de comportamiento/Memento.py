from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits


class Originador():
    """
    El Originador contiene un estado importante que puede cambiar con el tiempo. También
    define un método para guardar el estado dentro de un memento y otro método para
    restaurar el estado desde él.
    """

    _estado = None
    """
    Por simplicidad, el estado del originador se almacena en una única variable.
    """

    def __init__(self, estado: str) -> None:
        self._estado = estado
        print(f"Originador: Mi estado inicial es: {self._estado}")

    def hacer_algo(self) -> None:
        """
        La lógica empresarial del originador puede afectar su estado interno.
        Por lo tanto, el cliente debe hacer una copia de seguridad del estado antes de
        ejecutar métodos de la lógica empresarial mediante el método save().
        """

        print("Originador: Estoy haciendo algo importante.")
        self._estado = self._generar_cadena_aleatoria(30)
        print(f"Originador: y mi estado ha cambiado a: {self._estado}")

    def _generar_cadena_aleatoria(self, longitud: int = 10) -> None:
        return "".join(sample(ascii_letters, longitud))

    def guardar(self) -> Memento:
        """
        Guarda el estado actual dentro de un memento.
        """

        return MementoConcreto(self._estado)

    def restaurar(self, memento: Memento) -> None:
        """
        Restaura el estado del Originador desde un objeto memento.
        """

        self._estado = memento.obtener_estado()
        print(f"Originador: Mi estado ha cambiado a: {self._estado}")


class Memento(ABC):
    """
    La interfaz Memento proporciona una forma de recuperar los metadatos del
    memento, como la fecha de creación o el nombre. Sin embargo, no expone el
    estado del Originador.
    """

    @abstractmethod
    def obtener_nombre(self) -> str:
        pass

    @abstractmethod
    def obtener_fecha(self) -> str:
        pass


class MementoConcreto(Memento):
    def __init__(self, estado: str) -> None:
        self._estado = estado
        self._fecha = str(datetime.now())[:19]

    def obtener_estado(self) -> str:
        """
        El Originador utiliza este método al restaurar su estado.
        """
        return self._estado

    def obtener_nombre(self) -> str:
        """
        Los demás métodos son utilizados por el Cuidador para mostrar metadatos.
        """

        return f"{self._fecha} / ({self._estado[0:9]}...)"

    def obtener_fecha(self) -> str:
        return self._fecha


class Cuidador():
    """
    El Cuidador no depende de la clase MementoConcreto. Por lo tanto, no
    tiene acceso al estado del originador, almacenado dentro del memento.
    Trabaja con todos los mementos a través de la interfaz Memento base.
    """

    def __init__(self, originador: Originador) -> None:
        self._mementos = []
        self._originador = originador

    def respaldar(self) -> None:
        print("\nCuidador: Guardando estado del Originador...")
        self._mementos.append(self._originador.guardar())

    def deshacer(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Cuidador: Restaurando estado a: {memento.obtener_nombre()}")
        try:
            self._originador.restaurar(memento)
        except Exception:
            self.deshacer()

    def mostrar_historia(self) -> None:
        print("Cuidador: Aquí está la lista de mementos:")
        for memento in self._mementos:
            print(memento.obtener_nombre())


if __name__ == "__main__":
    originador = Originador("Super-duper-super-genial-super.")
    cuidador = Cuidador(originador)

    cuidador.respaldar()
    originador.hacer_algo()

    cuidador.respaldar()
    originador.hacer_algo()

    cuidador.respaldar()
    originador.hacer_algo()

    print()
    cuidador.mostrar_historia()

    print("\nCliente: ¡Ahora, vamos a deshacer!\n")
    cuidador.deshacer()

    print("\nCliente: ¡Una vez más!\n")
    cuidador.deshacer()
