from abc import ABC, abstractmethod


class Sujeto(ABC):
    """
    La interfaz Sujeto declara operaciones comunes tanto para RealSujeto como
    para Proxy. Mientras el cliente trabaje con RealSujeto utilizando esta
    interfaz, podrás pasarle un proxy en lugar de un sujeto real.
    """

    @abstractmethod
    def solicitud(self) -> None:
        pass


class RealSujeto(Sujeto):
    """
    El RealSujeto contiene cierta lógica empresarial principal. Por lo general,
    los RealSujetos son capaces de hacer algún trabajo útil que también puede
    ser muy lento o delicado, por ejemplo, corregir datos de entrada. Un Proxy
    puede resolver estos problemas sin realizar cambios en el código de RealSujeto.
    """

    def solicitud(self) -> None:
        print("RealSujeto: Manejando solicitud.")


class Proxy(Sujeto):
    """
    El Proxy tiene una interfaz idéntica a la de RealSujeto.
    """

    def __init__(self, real_sujeto: RealSujeto) -> None:
        self._real_sujeto = real_sujeto

    def solicitud(self) -> None:
        """
        Las aplicaciones más comunes del patrón Proxy son la carga diferida,
        el almacenamiento en caché, el control de acceso, el registro, etc. Un
        Proxy puede realizar una de estas tareas y luego, dependiendo del
        resultado, pasar la ejecución al mismo método en un objeto RealSujeto vinculado.
        """

        if self.verificar_acceso():
            self._real_sujeto.solicitud()
            self.registrar_acceso()

    def verificar_acceso(self) -> bool:
        print("Proxy: Verificando acceso antes de realizar una solicitud real.")
        return True

    def registrar_acceso(self) -> None:
        print("Proxy: Registrando el momento de la solicitud.", end="")


def codigo_cliente(sujeto: Sujeto) -> None:
    """
    Se supone que el código del cliente debe funcionar con todos los objetos
    (tanto sujetos como proxies) a través de la interfaz Sujeto para admitir tanto
    sujetos reales como proxies. En la vida real, sin embargo, los clientes
    trabajan principalmente con sus sujetos reales directamente. En este caso,
    para implementar el patrón de manera más fácil, puedes extender tu proxy a
    partir de la clase del sujeto real.
    """

    # ...

    sujeto.solicitud()

    # ...


if __name__ == "__main__":
    print("Cliente: Ejecutando el código del cliente con un sujeto real:")
    sujeto_real = RealSujeto()
    codigo_cliente(sujeto_real)

    print("")

    print("Cliente: Ejecutando el mismo código de cliente con un proxy:")
    proxy = Proxy(sujeto_real)
    codigo_cliente(proxy)
