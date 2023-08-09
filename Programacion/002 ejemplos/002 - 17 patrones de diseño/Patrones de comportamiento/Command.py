from __future__ import annotations
from abc import ABC, abstractmethod


class Comando(ABC):
    """
    La interfaz Comando declara un método para ejecutar un comando.
    """

    @abstractmethod
    def ejecutar(self) -> None:
        pass


class ComandoSimple(Comando):
    """
    Algunos comandos pueden implementar operaciones simples por sí mismos.
    """

    def __init__(self, carga: str) -> None:
        self._carga = carga

    def ejecutar(self) -> None:
        print(  f"ComandoSimple: Mira, puedo hacer cosas simples como imprimir"
                f" ({self._carga})")


class ComandoComplejo(Comando):
    """
    Sin embargo, algunos comandos pueden delegar operaciones más complejas a otros
    objetos llamados "receptores".
    """

    def __init__(self, receptor: Receptor, a: str, b: str) -> None:
        """
        Los comandos complejos pueden aceptar uno o varios objetos receptores junto con
        cualquier dato de contexto a través del constructor.
        """

        self._receptor = receptor
        self._a = a
        self._b = b

    def ejecutar(self) -> None:
        """
        Los comandos pueden delegar a cualquier método de un receptor.
        """

        print("ComandoComplejo: Tareas complejas deben ser realizadas por un objeto receptor", end="")
        self._receptor.hacer_algo(self._a)
        self._receptor.hacer_algo_mas(self._b)


class Receptor:
    """
    Las clases Receptor contienen lógica de negocio importante. Saben cómo realizar
    todo tipo de operaciones asociadas con llevar a cabo una solicitud. De hecho,
    cualquier clase puede servir como un Receptor.
    """

    def hacer_algo(self, a: str) -> None:
        print(f"\nReceptor: Trabajando en ({a}.)", end="")

    def hacer_algo_mas(self, b: str) -> None:
        print(f"\nReceptor: También trabajando en ({b}.)", end="")


class Invocador:
    """
    El Invocador está asociado con uno o varios comandos. Envía una solicitud
    al comando.
    """

    _al_inicio = None
    _al_fin = None

    """
    Inicializa los comandos.
    """

    def set_al_inicio(self, comando: Comando):
        self._al_inicio = comando

    def set_al_fin(self, comando: Comando):
        self._al_fin = comando

    def hacer_algo_importante(self) -> None:
        """
        El Invocador no depende de clases de comando o receptor concretas. El
        Invocador pasa una solicitud a un receptor indirectamente, ejecutando un
        comando.
        """

        print("Invocador: ¿Alguien quiere hacer algo antes de que comience?")
        if isinstance(self._al_inicio, Comando):
            self._al_inicio.ejecutar()

        print("Invocador: ...haciendo algo realmente importante...")

        print("Invocador: ¿Alguien quiere hacer algo después de que termine?")
        if isinstance(self._al_fin, Comando):
            self._al_fin.ejecutar()


if __name__ == "__main__":
    """
    El código del cliente puede parametrizar un invocador con cualquier comando.
    """

    invocador = Invocador()
    invocador.set_al_inicio(ComandoSimple("¡Di Hola!"))
    receptor = Receptor()
    invocador.set_al_fin(ComandoComplejo(receptor, "Enviar correo", "Guardar informe"))

    invocador.hacer_algo_importante()
