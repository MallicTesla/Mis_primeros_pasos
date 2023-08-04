# from __future__ import annotations
# from abc import ABC, abstractmethod


# class Abstraccion:
#     """
#     La Abstraccion define la interfaz para la parte de "control" de las dos
#     jerarquías de clase. Mantiene una referencia a un objeto de la jerarquía de
#     Implementacion y delega todo el trabajo real a este objeto.
#     """

#     def __init__(self, implementacion: Implementacion) -> None:
#         self.implementacion = implementacion

#     def operacion(self) -> str:
#         return (f"Abstraccion: Operación base con:\n"
#                 f"{self.implementacion.operacion_implementacion()}")


# class AbstraccionExtendida(Abstraccion):
#     """
#     Puedes extender la Abstraccion sin cambiar las clases de Implementacion.
#     """

#     def operacion(self) -> str:
#         return (f"AbstraccionExtendida: Operación extendida con:\n"
#                 f"{self.implementacion.operacion_implementacion()}")


# class Implementacion(ABC):
#     """
#     La Implementacion define la interfaz para todas las clases de implementación.
#     No tiene por qué coincidir con la interfaz de la Abstraccion. De hecho, las
#     dos interfaces pueden ser completamente diferentes. Normalmente, la
#     interfaz de Implementacion proporciona solo operaciones primitivas, mientras
#     que la Abstraccion define operaciones de más alto nivel basadas en esas
#     primitivas.
#     """

#     @abstractmethod
#     def operacion_implementacion(self) -> str:
#         pass


# """
# Cada Implementacion Concreta corresponde a una plataforma específica e
# implementa la interfaz de Implementacion utilizando la API de esa plataforma.
# """


# class ImplementacionConcretaA(Implementacion):
#     def operacion_implementacion(self) -> str:
#         return "ImplementacionConcretaA: Aquí está el resultado en la plataforma A."


# class ImplementacionConcretaB(Implementacion):
#     def operacion_implementacion(self) -> str:
#         return "ImplementacionConcretaB: Aquí está el resultado en la plataforma B."


# def codigo_cliente(abstraccion: Abstraccion) -> None:
#     """
#     Excepto en la fase de inicialización, donde un objeto Abstraccion se enlaza
#     con un objeto Implementacion específico, el código del cliente debe depender
#     solo de la clase Abstraccion. De esta manera, el código del cliente puede
#     admitir cualquier combinación de abstraccion-implementacion preconfigurada.
#     """

#     # ...

#     print(abstraccion.operacion(), end="")

#     # ...


# if __name__ == "__main__":
#     """
#     El código del cliente debe ser capaz de funcionar con cualquier combinación
#     preconfigurada de abstraccion-implementacion.
#     """

#     implementacion = ImplementacionConcretaA()
#     abstraccion = Abstraccion(implementacion)
#     codigo_cliente(abstraccion)

#     print("\n")

#     implementacion = ImplementacionConcretaB()
#     abstraccion = AbstraccionExtendida(implementacion)
#     codigo_cliente(abstraccion)









from __future__ import annotations
from abc import ABC, abstractmethod

# Interface Implementacion
class ColorImplementacion(ABC):
    @abstractmethod
    def cambiar_color(self, color: str) -> str:
        pass

# Implementaciones Concretas
class ColorRojo(ColorImplementacion):
    def cambiar_color(self, color: str) -> str:
        return f"Cambiando el color a {color} rojo."

class ColorAzul(ColorImplementacion):
    def cambiar_color(self, color: str) -> str:
        return f"Cambiando el color a {color} azul."

# Clase Abstraccion
class Juguete(ABC):
    def __init__(self, color: ColorImplementacion) -> None:
        self.color = color

    @abstractmethod
    def encender(self) -> str:
        pass

    @abstractmethod
    def apagar(self) -> str:
        pass

    def cambiar_color(self, color: str) -> str:
        return self.color.cambiar_color(color)

# Implementaciones Concretas de la Clase Abstraccion
class Carro(Juguete):
    def encender(self) -> str:
        return "Carro: Encendido."

    def apagar(self) -> str:
        return "Carro: Apagado."

class Robot(Juguete):
    def encender(self) -> str:
        return "Robot: Activado."

    def apagar(self) -> str:
        return "Robot: Desactivado."

if __name__ == "__main__":
    color_rojo = ColorRojo()
    color_azul = ColorAzul()

    carro_rojo = Carro(color_rojo)
    robot_azul = Robot(color_azul)

    print(carro_rojo.encender())
    print(carro_rojo.cambiar_color("azul"))
    print(carro_rojo.apagar())

    print("\n")

    print(robot_azul.encender())
    print(robot_azul.cambiar_color("verde"))
    print(robot_azul.apagar())
