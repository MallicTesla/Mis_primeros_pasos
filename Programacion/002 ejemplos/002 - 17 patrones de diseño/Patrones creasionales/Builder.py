from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Constructor(ABC):
    """
    La interfaz Constructor especifica métodos para crear las diferentes partes
    de los objetos Producto.
    """

    @property
    @abstractmethod
    def producto(self) -> None:
        pass

    @abstractmethod
    def producir_parte_a(self) -> None:
        pass

    @abstractmethod
    def producir_parte_b(self) -> None:
        pass

    @abstractmethod
    def producir_parte_c(self) -> None:
        pass


class ConstructorConcreto1(Constructor):
    """
    Las clases ConstructorConcreto siguen la interfaz Constructor y proporcionan
    implementaciones específicas de los pasos de construcción. Tu programa puede
    tener varias variaciones de Constructores implementadas de manera diferente.
    """

    def __init__(self) -> None:
        """
        Una nueva instancia de constructor debe contener un objeto de producto en blanco,
        que se utiliza en el ensamblaje posterior.
        """
        self.reiniciar()

    def reiniciar(self) -> None:
        self._producto = Producto1()

    @property
    def producto(self) -> Producto1:
        """
        Los Constructores Concretos deben proporcionar sus propios métodos para
        recuperar resultados. Esto se debe a que varios tipos de constructores
        pueden crear productos completamente diferentes que no siguen la misma
        interfaz. Por lo tanto, tales métodos no se pueden declarar en la interfaz
        base Constructor (al menos en un lenguaje de programación de tipo estático).

        Por lo general, después de devolver el resultado final al cliente, se espera
        que una instancia de constructor esté lista para comenzar a producir otro producto.
        Por eso es una práctica habitual llamar al método de reinicio al final del
        cuerpo del método `obtener_producto`. Sin embargo, este comportamiento no es
        obligatorio y puedes hacer que tus constructores esperen una llamada de reinicio
        explícita desde el código del cliente antes de desechar el resultado anterior.
        """
        producto = self._producto
        self.reiniciar()
        return producto

    def producir_parte_a(self) -> None:
        self._producto.agregar("ParteA1")

    def producir_parte_b(self) -> None:
        self._producto.agregar("ParteB1")

    def producir_parte_c(self) -> None:
        self._producto.agregar("ParteC1")


class Producto1():
    """
    Tiene sentido utilizar el patrón Constructor solo cuando tus productos son
    bastante complejos y requieren una configuración extensa.

    A diferencia de otros patrones creacionales, los Constructores Concretos pueden
    producir productos no relacionados. En otras palabras, los resultados de varios
    constructores no siempre siguen la misma interfaz.
    """

    def __init__(self) -> None:
        self.piezas = []

    def agregar(self, parte: Any) -> None:
        self.piezas.append(parte)

    def listar_partes(self) -> None:
        print(f"Partes del producto: {', '.join(self.piezas)}", end="")


class Director:
    """
    El Director solo es responsable de ejecutar los pasos de construcción en un
    orden particular. Es útil cuando se producen productos según un orden o
    configuración específicos. Hablando estrictamente, la clase Director es
    opcional, ya que el código del cliente puede controlar los constructores
    directamente.
    """

    def __init__(self) -> None:
        self._constructor = None

    @property
    def constructor(self) -> Constructor:
        return self._constructor

    @constructor.setter
    def constructor(self, constructor: Constructor) -> None:
        """
        El Director funciona con cualquier instancia de constructor que el código
        del cliente le pase. De esta manera, el código del cliente puede alterar
        el tipo final del producto recién ensamblado.
        """
        self._constructor = constructor

    """
    El Director puede construir varias variaciones del producto utilizando los
    mismos pasos de construcción.
    """

    def construir_producto_minimo_viable(self) -> None:
        self.constructor.producir_parte_a()

    def construir_producto_completo(self) -> None:
        self.constructor.producir_parte_a()
        self.constructor.producir_parte_b()
        self.constructor.producir_parte_c()


if __name__ == "__main__":
    """
    El código del cliente crea un objeto constructor, lo pasa al director y luego
    inicia el proceso de construcción. El resultado final se recupera del objeto
    constructor.
    """

    director = Director()
    constructor = ConstructorConcreto1()
    director.constructor = constructor

    print("Producto básico estándar: ")
    director.construir_producto_minimo_viable()
    constructor.producto.listar_partes()

    print("\n")

    print("Producto completo estándar: ")
    director.construir_producto_completo()
    constructor.producto.listar_partes()

    print("\n")

    # Recuerda, el patrón Constructor se puede usar sin una clase Director.
    print("Producto personalizado: ")
    constructor.producir_parte_a()
    constructor.producir_parte_b()
    constructor.producto.listar_partes()
