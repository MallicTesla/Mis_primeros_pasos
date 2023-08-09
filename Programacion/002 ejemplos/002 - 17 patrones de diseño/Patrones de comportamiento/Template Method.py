from abc import ABC, abstractmethod


class ClaseAbstracta(ABC):
    """
    La Clase Abstracta define un método de plantilla que contiene una estructura de
    algún algoritmo, compuesto por llamadas a operaciones primitivas (usualmente) abstractas.

    Las subclases concretas deben implementar estas operaciones, pero deben dejar el
    método de plantilla en sí intacto.
    """

    def metodo_plantilla(self) -> None:
        """
        El método de plantilla define la estructura de un algoritmo.
        """

        self.operacion_base1()
        self.operaciones_requeridas1()
        self.operacion_base2()
        self.gancho1()
        self.operaciones_requeridas2()
        self.operacion_base3()
        self.gancho2()

    # Estas operaciones ya tienen implementaciones.

    def operacion_base1(self) -> None:
        print("ClaseAbstracta dice: Estoy haciendo la mayor parte del trabajo")

    def operacion_base2(self) -> None:
        print("ClaseAbstracta dice: Pero permito a las subclases anular algunas operaciones")

    def operacion_base3(self) -> None:
        print("ClaseAbstracta dice: Pero de todos modos estoy haciendo la mayor parte del trabajo")

    # Estas operaciones deben ser implementadas en las subclases.

    @abstractmethod
    def operaciones_requeridas1(self) -> None:
        pass

    @abstractmethod
    def operaciones_requeridas2(self) -> None:
        pass

    # Estos son "ganchos". Las subclases pueden anularlos, pero no es obligatorio,
    # ya que los ganchos ya tienen una implementación predeterminada (pero vacía).
    # Los ganchos proporcionan puntos de extensión adicionales en lugares cruciales del algoritmo.

    def gancho1(self) -> None:
        pass

    def gancho2(self) -> None:
        pass


class ClaseConcreta1(ClaseAbstracta):
    """
    Las clases concretas deben implementar todas las operaciones abstractas de la
    clase base. También pueden anular algunas operaciones con una implementación predeterminada.
    """

    def operaciones_requeridas1(self) -> None:
        print("ClaseConcreta1 dice: Operación1 implementada")

    def operaciones_requeridas2(self) -> None:
        print("ClaseConcreta1 dice: Operación2 implementada")


class ClaseConcreta2(ClaseAbstracta):
    """
    Por lo general, las clases concretas solo anulan una fracción de las operaciones
    de la clase base.
    """

    def operaciones_requeridas1(self) -> None:
        print("ClaseConcreta2 dice: Operación1 implementada")

    def operaciones_requeridas2(self) -> None:
        print("ClaseConcreta2 dice: Operación2 implementada")

    def gancho1(self) -> None:
        print("ClaseConcreta2 dice: Gancho1 anulado")


def codigo_cliente(clase_abstracta: ClaseAbstracta) -> None:
    """
    El código del cliente llama al método de plantilla para ejecutar el algoritmo.
    El código del cliente no tiene que conocer la clase concreta de un objeto con el que trabaja,
    siempre que trabaje con objetos a través de la interfaz de su clase base.
    """

    # ...
    clase_abstracta.metodo_plantilla()
    # ...


if __name__ == "__main__":
    print("El mismo código del cliente puede funcionar con diferentes subclases:")
    codigo_cliente(ClaseConcreta1())
    print("")

    print("El mismo código del cliente puede funcionar con diferentes subclases:")
    codigo_cliente(ClaseConcreta2())
