from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


"""
Para crear un iterador en Python, existen dos clases abstractas en el módulo
built-in `collections` - Iterable, Iterator. Necesitamos implementar el
método `__iter__()` en el objeto iterado (colección) y el método `__next__ ()`
en el iterador.
"""


class IteradorOrdenAlfabetico(Iterator):
    """
    Los Iteradores Concretos implementan varios algoritmos de recorrido. Estas
    clases almacenan la posición actual de recorrido en todo momento.
    """

    """
    El atributo `_position` almacena la posición actual de recorrido. Un iterador
    puede tener muchos otros campos para almacenar el estado de la iteración,
    especialmente cuando se supone que debe trabajar con un tipo particular de
    colección.
    """
    _position: int = None

    """
    Este atributo indica la dirección del recorrido.
    """
    _reverse: bool = False

    def __init__(self, coleccion: ColeccionPalabras, reverse: bool = False) -> None:
        self._coleccion = coleccion
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        El método __next__() debe devolver el siguiente elemento en la secuencia. Al
        llegar al final, y en llamadas posteriores, debe generar StopIteration.
        """
        try:
            valor = self._coleccion[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return valor


class ColeccionPalabras(Iterable):
    """
    Las Colecciones Concretas proporcionan uno o varios métodos para obtener
    instancias frescas de iteradores, compatibles con la clase de colección.
    """

    def __init__(self, coleccion: List[Any] = []) -> None:
        self._coleccion = coleccion

    def __iter__(self) -> IteradorOrdenAlfabetico:
        """
        El método __iter__() devuelve el objeto iterador en sí mismo, por defecto
        devolvemos el iterador en orden ascendente.
        """
        return IteradorOrdenAlfabetico(self._coleccion)

    def obtener_iterador_inverso(self) -> IteradorOrdenAlfabetico:
        return IteradorOrdenAlfabetico(self._coleccion, True)

    def agregar_item(self, item: Any):
        self._coleccion.append(item)


if __name__ == "__main__":
    # El código del cliente puede o no conocer las clases de Iterador o Colección Concreta,
    # dependiendo del nivel de indirección que desee mantener en su programa.
    coleccion = ColeccionPalabras()
    coleccion.agregar_item("Primero")
    coleccion.agregar_item("Segundo")
    coleccion.agregar_item("Tercero")

    print("Recorrido directo:")
    print("\n".join(coleccion))
    print("")

    print("Recorrido inverso:")
    print("\n".join(coleccion.obtener_iterador_inverso()), end="")
