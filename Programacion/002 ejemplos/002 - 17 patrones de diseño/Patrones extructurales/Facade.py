from __future__ import annotations


class Fachada:
    """
    La clase Fachada proporciona una interfaz simple a la lógica compleja de uno o
    varios subsistemas. La Fachada delega las solicitudes del cliente a los
    objetos apropiados dentro del subsistema. La Fachada también es responsable de
    gestionar su ciclo de vida. Todo esto protege al cliente de la complejidad no deseada
    del subsistema.
    """

    def __init__(self, subsistema1: Subsistema1, subsistema2: Subsistema2) -> None:
        """
        Dependiendo de las necesidades de tu aplicación, puedes proporcionarle a la Fachada
        objetos de subsistemas existentes o forzar a la Fachada a crearlos por sí misma.
        """

        self._subsistema1 = subsistema1 or Subsistema1()
        self._subsistema2 = subsistema2 or Subsistema2()

    def operacion(self) -> str:
        """
        Los métodos de la Fachada son atajos convenientes para la funcionalidad sofisticada
        de los subsistemas. Sin embargo, los clientes solo acceden a una fracción
        de las capacidades de un subsistema.
        """

        resultados = []
        resultados.append("La Fachada inicializa los subsistemas:")
        resultados.append(self._subsistema1.operacion1())
        resultados.append(self._subsistema2.operacion1())
        resultados.append("La Fachada ordena a los subsistemas que realicen la acción:")
        resultados.append(self._subsistema1.operacion_n())
        resultados.append(self._subsistema2.operacion_z())
        return "\n".join(resultados)


class Subsistema1:
    """
    El Subsistema puede aceptar solicitudes tanto de la fachada como directamente del cliente.
    En cualquier caso, para el Subsistema, la Fachada es simplemente otro cliente, y no es
    parte del Subsistema.
    """

    def operacion1(self) -> str:
        return "Subsistema1: ¡Listo!"

    # ...

    def operacion_n(self) -> str:
        return "Subsistema1: ¡Vamos!"


class Subsistema2:
    """
    Algunas fachadas pueden trabajar con múltiples subsistemas al mismo tiempo.
    """

    def operacion1(self) -> str:
        return "Subsistema2: ¡Prepárense!"

    # ...

    def operacion_z(self) -> str:
        return "Subsistema2: ¡Fuego!"


def codigo_cliente(fachada: Fachada) -> None:
    """
    El código cliente trabaja con subsistemas complejos a través de una interfaz simple
    proporcionada por la Fachada. Cuando una fachada gestiona el ciclo de vida del
    subsistema, el cliente podría ni siquiera saber sobre la existencia del
    subsistema. Este enfoque permite mantener la complejidad bajo control.
    """

    print(fachada.operacion(), end="")


if __name__ == "__main__":
    # El código cliente puede tener algunos de los objetos del subsistema ya creados.
    # En este caso, puede ser conveniente inicializar la Fachada con estos
    # objetos en lugar de permitir que la Fachada cree nuevas instancias.
    subsistema1 = Subsistema1()
    subsistema2 = Subsistema2()
    fachada = Fachada(subsistema1, subsistema2)
    print ("...")
    codigo_cliente(fachada)
