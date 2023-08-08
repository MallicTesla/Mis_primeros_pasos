from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Manejador(ABC):
    """
    La interfaz Manejador declara un método para construir la cadena de
    manejadores. También declara un método para ejecutar una solicitud.
    """

    @abstractmethod
    def establecer_siguiente(self, manejador: Manejador) -> Manejador:
        pass

    @abstractmethod
    def manejar(self, solicitud) -> Optional[str]:
        pass


class ManejadorAbstracto(Manejador):
    """
    El comportamiento predeterminado de encadenamiento se puede implementar
    dentro de una clase base de manejador.
    """

    _siguiente_manejador: Manejador = None

    def establecer_siguiente(self, manejador: Manejador) -> Manejador:
        self._siguiente_manejador = manejador
        # Devolver un manejador desde aquí nos permitirá enlazar los manejadores de
        # manera conveniente como en esta línea:
        # mono.establecer_siguiente(ardilla).establecer_siguiente(perro)
        return manejador

    @abstractmethod
    def manejar(self, solicitud: Any) -> str:
        if self._siguiente_manejador:
            return self._siguiente_manejador.manejar(solicitud)

        return None


"""
Todos los Manejadores Concretos manejan una solicitud o la pasan al siguiente
manejador en la cadena.
"""


class ManejadorMono(ManejadorAbstracto):
    def manejar(self, solicitud: Any) -> str:
        if solicitud == "Banana":
            return f"Mono: Voy a comer la {solicitud}"
        else:
            return super().manejar(solicitud)


class ManejadorArdilla(ManejadorAbstracto):
    def manejar(self, solicitud: Any) -> str:
        if solicitud == "Nuez":
            return f"Ardilla: Voy a comer la {solicitud}"
        else:
            return super().manejar(solicitud)


class ManejadorPerro(ManejadorAbstracto):
    def manejar(self, solicitud: Any) -> str:
        if solicitud == "Albóndiga":
            return f"Perro: Voy a comer la {solicitud}"
        else:
            return super().manejar(solicitud)


def codigo_cliente(manejador: Manejador) -> None:
    """
    El código del cliente generalmente está diseñado para funcionar con un solo
    manejador. En la mayoría de los casos, ni siquiera sabe que el manejador es
    parte de una cadena.
    """

    for alimento in ["Nuez", "Banana", "Taza de café"]:
        print(f"\nCliente: ¿Quién quiere una {alimento}?")
        resultado = manejador.manejar(alimento)
        if resultado:
            print(f"  {resultado}", end="")
        else:
            print(f"  {alimento} quedó intacto.", end="")


if __name__ == "__main__":
    mono = ManejadorMono()
    ardilla = ManejadorArdilla()
    perro = ManejadorPerro()

    mono.establecer_siguiente(ardilla).establecer_siguiente(perro)

    # El cliente debería poder enviar una solicitud a cualquier manejador, no solo al
    # primero en la cadena.
    print("Cadena: Mono > Ardilla > Perro")
    codigo_cliente(mono)
    print("\n")

    print("Subcadena: Ardilla > Perro")
    codigo_cliente(ardilla)
