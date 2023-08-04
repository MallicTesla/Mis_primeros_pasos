from __future__ import annotations
from abc import ABC, abstractmethod


class Creador(ABC):
    """
    La clase Creador declara el método de fábrica que debe devolver un objeto de la clase Producto.
    Las subclases de Creador suelen proporcionar la implementación de este método.
    """

    @abstractmethod
    def metodo_de_fabrica(self):
        """
        Nótese que el Creador también puede proporcionar alguna implementación predeterminada
        del método de fábrica.
        """
        pass

    def alguna_operacion(self) -> str:
        """
        Aunque se llame 'alguna_operacion', la responsabilidad principal del Creador no es
        crear productos. Generalmente, contiene lógica de negocio central que depende de objetos
        Producto devueltos por el método de fábrica. Las subclases pueden cambiar indirectamente
        esa lógica de negocio al sobrescribir el método de fábrica y devolver un tipo de producto
        diferente.
        """

        # Llama al método de fábrica para crear un objeto Producto.
        producto = self.metodo_de_fabrica()

        # Ahora, usa el producto.
        resultado = f"Creador: El mismo código del creador acaba de trabajar con {producto.operacion()}"

        return resultado


"""
Los Creadores concretos sobrescriben el método de fábrica para cambiar el tipo de producto resultante.
"""


class CreadorConcreto1(Creador):
    """
    Nótese que la firma del método sigue utilizando el tipo de producto abstracto,
    aunque el producto concreto se devuelve realmente desde el método. De esta manera,
    el Creador puede seguir siendo independiente de las clases de producto concretas.
    """

    def metodo_de_fabrica(self) -> Producto:
        return ProductoConcreto1()


class CreadorConcreto2(Creador):
    def metodo_de_fabrica(self) -> Producto:
        return ProductoConcreto2()


class Producto(ABC):
    """
    La interfaz Producto declara las operaciones que todos los productos concretos deben implementar.
    """

    @abstractmethod
    def operacion(self) -> str:
        pass


"""
Los Productos concretos proporcionan varias implementaciones de la interfaz Producto.
"""


class ProductoConcreto1(Producto):
    def operacion(self) -> str:
        return "{Resultado del ProductoConcreto1}"


class ProductoConcreto2(Producto):
    def operacion(self) -> str:
        return "{Resultado del ProductoConcreto2}"


def codigo_cliente(creador: Creador) -> None:
    """
    El código del cliente trabaja con una instancia de un creador concreto, aunque a través de
    su interfaz base. Siempre que el cliente siga trabajando con el creador a través de la
    interfaz base, puede pasarse cualquier subclase de creador.
    """

    print(  f"Cliente: No conozco la clase del creador, pero aún funciona.\n"
            f"{creador.alguna_operacion()}", end="")


if __name__ == "__main__":
    print("Aplicación: Lanzada con CreadorConcreto1.")
    codigo_cliente(CreadorConcreto1())
    print("\n")

    print("Aplicación: Lanzada con CreadorConcreto2.")
    codigo_cliente(CreadorConcreto2())
