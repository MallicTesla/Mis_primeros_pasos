import copy

class EntidadReferenciada:
    def __init__(self):
        self.padre = None

    def establecer_padre(self, padre):
        self.padre = padre

class AlgunComponente:
    """
    Python proporciona su propia interfaz de prototipo a través de las funciones
    `copy.copy` y `copy.deepcopy`. Cualquier clase que quiera implementar
    implementaciones personalizadas debe sobrescribir las funciones miembro
    `__copy__` y `__deepcopy__`.
    """

    def __init__(self, algun_entero, alguna_lista_de_objetos, alguna_referencia_circular):
        self.algun_entero = algun_entero
        self.alguna_lista_de_objetos = alguna_lista_de_objetos
        self.alguna_referencia_circular = alguna_referencia_circular

    def __copy__(self):
        """
        Crea una copia superficial. Este método se llamará cada vez que alguien
        llame a `copy.copy` con este objeto y el valor devuelto se usará como la
        nueva copia superficial.
        """

        # Primero, creemos copias de los objetos anidados.
        alguna_lista_de_objetos = copy.copy(self.alguna_lista_de_objetos)
        alguna_referencia_circular = copy.copy(self.alguna_referencia_circular)

        # Luego, clonemos el objeto en sí, usando las copias preparadas de los
        # objetos anidados.
        nuevo = self.__class__(
            self.algun_entero, alguna_lista_de_objetos, alguna_referencia_circular
        )
        nuevo.__dict__.update(self.__dict__)

        return nuevo

    def __deepcopy__(self, memo=None):
        """
        Crea una copia profunda. Este método se llamará cada vez que alguien
        llame a `copy.deepcopy` con este objeto y el valor devuelto se usará como
        la nueva copia profunda.

        ¿Cuál es el uso del argumento `memo`? Memo es el diccionario que utiliza
        la biblioteca `deepcopy` para evitar copias recursivas infinitas en
        instancias de referencias circulares. Pásalo a todas las llamadas de
        `deepcopy` que hagas en la implementación de `__deepcopy__` para evitar
        recursiones infinitas.
        """
        if memo is None:
            memo = {}

        # Primero, creemos copias de los objetos anidados.
        alguna_lista_de_objetos = copy.deepcopy(self.alguna_lista_de_objetos, memo)
        alguna_referencia_circular = copy.deepcopy(self.alguna_referencia_circular, memo)

        # Luego, clonemos el objeto en sí, usando las copias preparadas de los
        # objetos anidados.
        nuevo = self.__class__(
            self.algun_entero, alguna_lista_de_objetos, alguna_referencia_circular
        )
        nuevo.__dict__ = copy.deepcopy(self.__dict__, memo)

        return nuevo

if __name__ == "__main__":
    lista_de_objetos = [1, {1, 2, 3}, [1, 2, 3]]
    referencia_circular = EntidadReferenciada()
    componente = AlgunComponente(23, lista_de_objetos, referencia_circular)
    referencia_circular.establecer_padre(componente)

    componente_copiado_superficialmente = copy.copy(componente)

    # Veamos si al modificar la lista `alguna_lista_de_objetos` en
    # `componente_copiado_superficialmente`, también se modifica en `componente`.
    componente_copiado_superficialmente.alguna_lista_de_objetos.append("otro objeto")
    if componente.alguna_lista_de_objetos[-1] == "otro objeto":
        print(
            "Al agregar elementos a `alguna_lista_de_objetos` en `componente_copiado_superficialmente`, también se agrega a `componente.alguna_lista_de_objetos`."
        )
    else:
        print(
            "Al agregar elementos a `alguna_lista_de_objetos` en `componente_copiado_superficialmente`, no se agrega a `componente.alguna_lista_de_objetos`."
        )

    # Modifiquemos el conjunto en la lista de objetos.
    componente.alguna_lista_de_objetos[1].add(4)
    if 4 in componente_copiado_superficialmente.alguna_lista_de_objetos[1]:
        print(
            "Al cambiar objetos en `componente.alguna_lista_de_objetos`, también se cambia ese objeto en `componente_copiado_superficialmente.alguna_lista_de_objetos`."
        )
    else:
        print(
            "Al cambiar objetos en `componente.alguna_lista_de_objetos`, no se cambia ese objeto en `componente_copiado_superficialmente.alguna_lista_de_objetos`."
        )

    componente_copiado_profundamente = copy.deepcopy(componente)

    # Veamos si al modificar la lista `alguna_lista_de_objetos` en
    # `componente_copiado_profundamente`, también se modifica en `componente`.
    componente_copiado_profundamente.alguna_lista_de_objetos.append("un objeto más")
    if componente.alguna_lista_de_objetos[-1] == "un objeto más":
        print(
            "Al agregar elementos a `alguna_lista_de_objetos` en `componente_copiado_profundamente`, también se agrega a `componente.alguna_lista_de_objetos`."
        )
    else:
        print(
            "Al agregar elementos a `alguna_lista_de_objetos` en `componente_copiado_profundamente`, no se agrega a `componente.alguna_lista_de_objetos`."
        )

    # Modifiquemos el conjunto en la lista de objetos.
    componente.alguna_lista_de_objetos[1].add(10)
    if 10 in componente_copiado_profundamente.alguna_lista_de_objetos[1]:
        print(
            "Al cambiar objetos en `componente.alguna_lista_de_objetos`, también se cambia ese objeto en `componente_copiado_profundamente.alguna_lista_de_objetos`."
        )
    else:
        print(
            "Al cambiar objetos en `componente.alguna_lista_de_objetos`, no se cambia ese objeto en `componente_copiado_profundamente.alguna_lista_de_objetos`."
        )

    print(
        f"id(componente_copiado_profundamente.alguna_referencia_circular.padre): {id(componente_copiado_profundamente.alguna_referencia_circular.padre)}"
    )
    print(
        f"id(componente_copiado_profundamente.alguna_referencia_circular.padre.alguna_referencia_circular.padre): {id(componente_copiado_profundamente.alguna_referencia_circular.padre.alguna_referencia_circular.padre)}"
    )
    print(
        "^^ Esto muestra que los objetos copiados profundamente contienen la misma referencia, no se clonan repetidamente."
    )
