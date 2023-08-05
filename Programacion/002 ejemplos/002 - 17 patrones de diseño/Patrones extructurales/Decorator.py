class Componente():
    """
    La interfaz base Componente define operaciones que pueden ser alteradas por los decoradores.
    """

    def operacion(self) -> str:
        pass


class ComponenteConcreto(Componente):
    """
    Los Componentes Concretos proporcionan implementaciones predeterminadas de las operaciones. Puede haber varias
    variaciones de estas clases.
    """

    def operacion(self) -> str:
        return "ComponenteConcreto"


class Decorador(Componente):
    """
    La clase Decorador base sigue la misma interfaz que los demás componentes. El propósito principal de esta clase
    es definir la interfaz de envoltura para todos los decoradores concretos. La implementación predeterminada del
    código de envoltura podría incluir un campo para almacenar un componente envuelto y los medios para inicializarlo.
    """

    _componente: Componente = None

    def __init__(self, componente: Componente) -> None:
        self._componente = componente

    @property
    def componente(self) -> Componente:
        """
        El Decorador delega todo el trabajo al componente envuelto.
        """

        return self._componente

    def operacion(self) -> str:
        return self._componente.operacion()


class DecoradorConcretoA(Decorador):
    """
    Los Decoradores Concretos llaman al objeto envuelto y alteran su resultado de alguna manera.
    """

    def operacion(self) -> str:
        """
        Los decoradores pueden llamar a la implementación principal de la operación, en lugar de
        llamar directamente al objeto envuelto. Este enfoque simplifica la extensión de las clases decoradoras.
        """
        return f"DecoradorConcretoA({self.componente.operacion()})"


class DecoradorConcretoB(Decorador):
    """
    Los decoradores pueden ejecutar su comportamiento antes o después de la llamada a un objeto envuelto.
    """

    def operacion(self) -> str:
        return f"DecoradorConcretoB({self.componente.operacion()})"


def codigo_cliente(componente: Componente) -> None:
    """
    El código del cliente funciona con todos los objetos utilizando la interfaz Componente. De esta manera, puede
    mantenerse independiente de las clases concretas de los componentes con los que trabaja.
    """

    # ...

    print(f"RESULTADO: {componente.operacion()}", end="")

    # ...


if __name__ == "__main__":
    # De esta manera, el código del cliente puede soportar tanto componentes simples...
    simple = ComponenteConcreto()
    print("Cliente: Tengo un componente simple:")
    codigo_cliente(simple)
    print("\n")

    # ...así como componentes decorados.
    #
    # Observa cómo los decoradores pueden envolver no solo componentes simples, sino también otros
    # decoradores.
    decorador1 = DecoradorConcretoA(simple)
    decorador2 = DecoradorConcretoB(decorador1)
    print("Cliente: Ahora tengo un componente decorado:")
    codigo_cliente(decorador2)