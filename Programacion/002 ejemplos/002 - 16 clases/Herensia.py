#   clase padre
class Pokemon () :
    def __init__(self, nombre, tipo) :
        self.nombre = nombre
        self.tipo = tipo

    def descripcion (self) :
        return f"{self.nombre} es de tipo {self.tipo}"

#   clase hijo o heredada
class Pikachu (Pokemon):
    def ataque (self, tipo_ataque):
        return f"{self.nombre} tipo de ataque {tipo_ataque}"

#   clase hijo o heredada
class Charmander (Pokemon):
    def ataque (self, tipo_ataque):
        return f"{self.nombre} tipo de ataque {tipo_ataque}"

#   asi relleno los atributos de la case padre
nuevo_pokemon = Pikachu ("Mallic", "electrico")
print (nuevo_pokemon.descripcion())

#   asi relleno los atributos de la clase hijo con el objeto ya creado
print (nuevo_pokemon.ataque("imack trueno"))

# -----------------------------------------------------------------------

class Calculadora:
    def __init__(self, numero):
        self.n = numero
        #   Crea una lista llamada datos dentro del objeto actual (self) con numero elementos, todos inicializados a 0.
        self.datos = [0 for i in range(numero)]

    def ingresar_dato(self):
        #   Crea una nueva lista llamada datos dentro del objeto actual (self) y la reemplaza con los valores ingresados por el usuario.
        #   El bucle for solicita al usuario ingresar self.n números y los almacena en la lista datos.
        self.datos = [int(input("Ingresar cifra " + str(i + 1) + " = ")) for i in range(self.n)]

class Op_Basicas(Calculadora):
    def __init__(self):
        #   Llama al constructor de la clase base o padre (Calculadora) con el argumento 2, lo que inicializará el objeto Op_Basicas con dos elementos en la lista datos.
        super().__init__(2)

    def suma(self):
        #   Desempaqueta los dos elementos de la lista datos y los asigna a las variables a y b.
        a, b = self.datos
        s = a + b
        print("El resultado es", s)

    def resta(self):
        a, b = self.datos
        r = a - b
        print("El resultado es", r)

class Raiz(Calculadora):
    def __init__(self):
        super().__init__(1)

    def cuadrada(self):
        import math
        a, = self.datos
        print("El resultado es:", math.sqrt(a))

ejemplo = Op_Basicas()
#   verifica si el objeto es una instancia de la clase especificada o de alguna de sus clases derivadas, y devuelve
print (isinstance (ejemplo, Op_Basicas))

#   es para verificar si una clase hereda de otra
print (issubclass(Op_Basicas, Calculadora))


