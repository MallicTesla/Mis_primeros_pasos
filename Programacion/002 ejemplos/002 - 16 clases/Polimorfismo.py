# class Animales :
#     def __init__(self, nombre) :
#         self.nombre = nombre

#     def tipo_animal (self) :
#         pass

# class Leon (Animales) :
#     def tipo_animal (self) :
#         print ("Leon animal salvaje")

# class Perro (Animales):
#     def tipo_animal(self):
#         print ("Perro animal domestico")

# nuevo_anmal_1 = Leon ("Tiger")
# nuevo_anmal_1.tipo_animal()

# nuevo_anmal_2 = Perro ("firulais")
# nuevo_anmal_2.tipo_animal()

# ----------------------------polimorfismo con funcion--------------------------

# class Tomate:
#     def tipo (self):
#         print ("Tomate es una fruta")

#     def color (self):
#         print ("rojo")

# class Manzana:
#     def tipo (self):
#         print ("la manzana es una fruta")

#     def color (self):
#         print ("verde")

# def funcion (objeto):
#     objeto.tipo ()
#     objeto.color ()

# nuevo_tomate = Tomate()
# funcion (nuevo_tomate)


# ------------------------------------------polimorfismo con metodos---------------------------------------------------------

# class Uruguay :
#     def capital (self):
#         print ("Montevideo")

#     def idioma (self):
#         print ("Español")

# class Italia :
#     def capital (self):
#         print ("Roma")

#     def idioma (self):
#         print ("Italiano")

# uruguayo =Uruguay()
# italiano = Italia()

# for pais in uruguayo, italiano :
#     pais.capital()
#     pais.idioma()


# ---------------------------------polimorfismo con herencias------------------------------------------------------------------------

class Aves :
    def volar (self):
        print("las malloria de las aves vuelan")

class Aguila (Aves):
    def volar(self):
        print ("las aguilas pueden volar")

class Piguino (Aves):
    def volar(self):
        print ("los pinguinos no puden volar")

ave = Aves()
ave.volar()

aguila = Aguila()
aguila.volar()

pinguino = Piguino()
pinguino.volar()











