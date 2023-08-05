class Objetivo:
    """
    El Objetivo define la interfaz específica del dominio utilizada por el código del cliente.
    """

    def solicitud(self) -> str:
        return "Objetivo: El comportamiento predeterminado del objetivo."


class Adaptable:
    """
    El Adaptable contiene un comportamiento útil, pero su interfaz es incompatible
    con el código del cliente existente. El Adaptable necesita una adaptación antes
    de que el código del cliente pueda usarlo.
    """

    def solicitud_especifica(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adaptador(Objetivo, Adaptable):
    """
    El Adaptador hace que la interfaz del Adaptable sea compatible con la interfaz
    del Objetivo a través de la herencia múltiple.
    """

    def solicitud(self) -> str:
        return f"Adaptador: (TRADUCIDO) {self.solicitud_especifica()[::-1]}"


def codigo_cliente(objetivo: "Objetivo") -> None:
    """
    El código del cliente admite todas las clases que siguen la interfaz del Objetivo.
    """

    print(objetivo.solicitud(), end="")


if __name__ == "__main__":
    print("Cliente: Puedo trabajar perfectamente con objetos Objetivo:")
    objetivo = Objetivo()
    codigo_cliente(objetivo)
    print("\n")

    adaptable = Adaptable()
    print(  "Cliente: La clase Adaptable tiene una interfaz extraña. "
            "Mira, no la entiendo:")
    print(f"Adaptable: {adaptable.solicitud_especifica()}", end="\n\n")

    print("Cliente: Pero puedo trabajar con ella a través del Adaptador:")
    adaptador = Adaptador()
    codigo_cliente(adaptador)