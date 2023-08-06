import json
from typing import Dict


class Flyweight():
    """
    El Flyweight almacena una porción común del estado (también llamado estado intrínseco)
    que pertenece a múltiples entidades empresariales reales. El Flyweight acepta el resto
    del estado (estado extrínseco, único para cada entidad) a través de sus parámetros de método.
    """

    def __init__(self, estado_compartido: str) -> None:
        self._estado_compartido = estado_compartido

    def operacion(self, estado_unico: str) -> None:
        s = json.dumps(self._estado_compartido)
        u = json.dumps(estado_unico)
        print(f"Flyweight: Mostrando estado compartido ({s}) y estado único ({u}).", end="")


class FabricaFlyweight():
    """
    La Fábrica de Flyweights crea y gestiona los objetos Flyweight. Asegura que los flyweights
    se compartan correctamente. Cuando el cliente solicita un flyweight, la fábrica devuelve una
    instancia existente o crea una nueva, si aún no existe.
    """

    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, flyweights_iniciales: Dict) -> None:
        for estado in flyweights_iniciales:
            self._flyweights[self.obtener_clave(estado)] = Flyweight(estado)

    def obtener_clave(self, estado: Dict) -> str:
        """
        Devuelve el hash de cadena de un Flyweight para un estado dado.
        """

        return "_".join(sorted(estado))

    def obtener_flyweight(self, estado_compartido: Dict) -> Flyweight:
        """
        Devuelve un Flyweight existente con un estado dado o crea uno nuevo.
        """

        clave = self.obtener_clave(estado_compartido)

        if not self._flyweights.get(clave):
            print("FabricaFlyweight: No se puede encontrar un flyweight, creando uno nuevo.")
            self._flyweights[clave] = Flyweight(estado_compartido)
        else:
            print("FabricaFlyweight: Reutilizando el flyweight existente.")

        return self._flyweights[clave]

    def listar_flyweights(self) -> None:
        cantidad = len(self._flyweights)
        print(f"FabricaFlyweight: Tengo {cantidad} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def agregar_auto_a_base_datos_policial(
    fabrica: FabricaFlyweight, placas: str, propietario: str,
    marca: str, modelo: str, color: str
) -> None:
    print("\n\nCliente: Agregando un auto a la base de datos.")
    flyweight = fabrica.obtener_flyweight([marca, modelo, color])
    # El código del cliente almacena o calcula el estado extrínseco y lo pasa
    # a los métodos del flyweight.
    flyweight.operacion([placas, propietario])


if __name__ == "__main__":
    """
    El código del cliente generalmente crea un montón de flyweights prellenados en la
    etapa de inicialización de la aplicación.
    """

    fabrica = FabricaFlyweight([
        ["Chevrolet", "Camaro2018", "rosado"],
        ["Mercedes Benz", "C300", "negro"],
        ["Mercedes Benz", "C500", "rojo"],
        ["BMW", "M5", "rojo"],
        ["BMW", "X6", "blanco"],
    ])

    fabrica.listar_flyweights()

    agregar_auto_a_base_datos_policial(
        fabrica, "CL234IR", "James Doe", "BMW", "M5", "rojo")

    agregar_auto_a_base_datos_policial(
        fabrica, "CL234IR", "James Doe", "BMW", "X1", "rojo")

    print("\n")

    fabrica.listar_flyweights()
