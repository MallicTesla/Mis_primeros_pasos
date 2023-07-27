from __future__ import annotations
from abc import ABC, abstractmethod


class FabricaAbstracta(ABC):
    """
    La interfaz FabricaAbstracta declara un conjunto de métodos que devuelven
    diferentes productos abstractos. Estos productos se denominan una familia
    y están relacionados por un tema o concepto de alto nivel. Los productos de
    una familia suelen poder colaborar entre sí. Una familia de productos puede
    tener varias variantes, pero los productos de una variante son incompatibles
    con los productos de otra.
    """
    @abstractmethod
    def crear_producto_a(self) -> ProductoAbstractoA:
        pass

    @abstractmethod
    def crear_producto_b(self) -> ProductoAbstractoB:
        pass


class FabricaConcreta1(FabricaAbstracta):
    """
    Las Fábricas Concretas producen una familia de productos que pertenecen a
    una sola variante. La fábrica garantiza que los productos resultantes sean
    compatibles. Tenga en cuenta que las firmas de los métodos de la Fábrica
    Concreta devuelven un producto abstracto, mientras que dentro del método se
    instancia un producto concreto.
    """

    def crear_producto_a(self) -> ProductoAbstractoA:
        return ProductoA1()

    def crear_producto_b(self) -> ProductoAbstractoB:
        return ProductoB1()


class FabricaConcreta2(FabricaAbstracta):
    """
    Cada Fábrica Concreta tiene una variante de producto correspondiente.
    """

    def crear_producto_a(self) -> ProductoAbstractoA:
        return ProductoA2()

    def crear_producto_b(self) -> ProductoAbstractoB:
        return ProductoB2()


class ProductoAbstractoA(ABC):
    """
    Cada producto distinto de una familia de productos debe tener una interfaz
    base. Todas las variantes del producto deben implementar esta interfaz.
    """

    @abstractmethod
    def funcion_util_a(self) -> str:
        pass


"""
Los Productos Concretos son creados por las correspondientes Fábricas Concretas.
"""


class ProductoA1(ProductoAbstractoA):
    def funcion_util_a(self) -> str:
        return "El resultado del producto A1."


class ProductoA2(ProductoAbstractoA):
    def funcion_util_a(self) -> str:
        return "El resultado del producto A2."


class ProductoAbstractoB(ABC):
    """
    Aquí está la interfaz base de otro producto. Todos los productos pueden
    interactuar entre sí, pero la interacción adecuada solo es posible entre
    productos de la misma variante concreta.
    """
    @abstractmethod
    def funcion_util_b(self) -> None:
        """
        El Producto B puede hacer su propia cosa...
        """
        pass

    @abstractmethod
    def otra_funcion_util_b(self, colaborador: ProductoAbstractoA) -> None:
        """
        ...pero también puede colaborar con ProductoA.

        La FabricaAbstracta se asegura de que todos los productos que crea sean
        de la misma variante y, por lo tanto, compatibles.
        """
        pass


"""
Los Productos Concretos son creados por las correspondientes Fábricas Concretas.
"""


class ProductoB1(ProductoAbstractoB):
    def funcion_util_b(self) -> str:
        return "El resultado del producto B1."

    """
    La variante Producto B1 solo puede funcionar correctamente con la variante
    Producto A1. Sin embargo, acepta cualquier instancia de ProductoAbstractoA
    como argumento.
    """

    def otra_funcion_util_b(self, colaborador: ProductoAbstractoA) -> str:
        result = colaborador.funcion_util_a()
        return f"El resultado del B1 colaborando con ({result})"


class ProductoB2(ProductoAbstractoB):
    def funcion_util_b(self) -> str:
        return "El resultado del producto B2."

    def otra_funcion_util_b(self, colaborador: ProductoAbstractoA):
        """
        La variante Producto B2 solo puede funcionar correctamente con la
        variante Producto A2. Sin embargo, acepta cualquier instancia de
        ProductoAbstractoA como argumento.
        """
        result = colaborador.funcion_util_a()
        return f"El resultado del B2 colaborando con ({result})"


def codigo_cliente(fabrica: FabricaAbstracta) -> None:
    """
    El código del cliente trabaja con fábricas y productos solo a través de
    tipos abstractos: FabricaAbstracta y ProductoAbstracto. Esto le permite
    pasar cualquier subclase de fábrica o producto al código del cliente sin
    romperlo.
    """
    producto_a = fabrica.crear_producto_a()
    producto_b = fabrica.crear_producto_b()

    print(f"{producto_b.funcion_util_b()}")
    print(f"{producto_b.otra_funcion_util_b(producto_a)}", end="")


if __name__ == "__main__":
    """
    El código del cliente puede trabajar con cualquier clase de fábrica concreta.
    """
    print("Cliente: Probando el código del cliente con el primer tipo de fábrica:")
    codigo_cliente(FabricaConcreta1())

    print("\n")

    print("Cliente: Probando el mismo código del cliente con el segundo tipo de fábrica:")
    codigo_cliente(FabricaConcreta2())
