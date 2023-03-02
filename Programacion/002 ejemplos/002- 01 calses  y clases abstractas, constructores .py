# #---------------------clase dinamica----------------------
# class dino:
#     _encendido = "primera variavle "        #   esto es un metodo "si tiene un _ no se deveria manipular fuera de la clase"

#     def apagado(self):                      #   esto es un metodo
#         self._encendido = False             #   el self. se usa para hacerle refencia a la variavle dentro de la clase

#     def encendido (self):
#         self._encendido = True

#     def Encendio (self):
#         return self._encendido;

# d1 = dino()                                 #   instanciar una clase contiene todos los metodos de la clas
#                                             #   antes de poder llamar un metodo primero ahi que instansear la clase

# print(d1._encendido)
# print(d1._encendido + "1")

# d1._encendido = "hola"                      #   el . se usa para llamar un metodo dentro de una clase
# print(d1._encendido)

# d1.encendido()
# print(d1._encendido)

# d1.apagado()
# print(d1._encendido)

# d2 = dino()                                 #   cada instansia no afecta a la otra

# print(d2._encendido)

# d2.encendido()
# print(d2._encendido)
# print(d2.Encendio())

# d2.apagado()
# print(d2._encendido)
# print(d2.Encendio())

# #---------------------------calse estatica------------------------------------------------------------------------------------------------
# #---------------------------calse estatica------------------------------------------------------------------------------------------------
# #---------------------------calse estatica------------------------------------------------------------------------------------------------

# # comparte el mismo espasio de memoria y se modifica

# class Estatica:
#     numero = 0 

#     def incrementa():
#         Estatica.numero += 1

# Estatica.incrementa()
# print(Estatica.numero)

# Estatica.incrementa()
# print(Estatica.numero)

# Estatica.incrementa()
# print(Estatica.numero)


# ---------------------------------calase eredada---------------------------------------------------------------------------------------------
# ---------------------------------calase eredada---------------------------------------------------------------------------------------------
# ---------------------------------calase eredada---------------------------------------------------------------------------------------------

#   las clases eradadas se usan para no repetir el mismo codigo dentro de otras clases
#   y la clase que se desea eredar se coloca dentro de los parentesis de las clases
#   

# class usuaria () :

#     def ocupante (self):
#         self.nombre = input ("nombre : ")
#         self.apellido = input ("apellido : ")

#     def estadia (self):
#         self.dias = int (input ("cuantos dias te quedas : "))

# class cuarto_01 (usuaria) :
#     _cuarto = "Cuarto 01"

#     def cama (self) :
#         self.plazas = int (input ("plasas de la cama : "))
#         self.color = input ("color_de_la_cama : ")
#     def baño (self) :
#         self.ducha = "si"

# class cuarto_02 (usuaria) :
#     _cuarto = "cuarto 02 "

#     def cama (self) :
#         self.plazas = int (input ("plasas de la cama : "))
#         self.color = input ("color_de_la_cama : ")

#     def baño (self) :
#         self.ducha = "no"

# A_01 = cuarto_01 ()
# A_01.ocupante ()
# A_01.estadia ()
# A_01.cama ()
# A_01.baño ()

# print(A_01._cuarto,"ocupante", A_01.nombre, A_01.apellido ,"dias",A_01.dias,"caracteristicas de la cama( plazas",A_01.plazas,"color",A_01.color,")")

# A_02 = cuarto_02 ()
# A_02.ocupante ()
# A_02.estadia ()
# A_02.cama ()
# A_02.baño ()

# print(f"{A_02._cuarto} ocupante {A_02.nombre} {A_02.apellido} dias {A_02.dias} caracteristicas de la cama ( plazas {A_02.plazas} color {A_02.color})")

#-------------------------------------------classe con constructor y destructor---------------------------------------------------------------
#-------------------------------------------classe con constructor y destructor---------------------------------------------------------------
#-------------------------------------------classe con constructor y destructor---------------------------------------------------------------

#   para crear un objeto es nesesario usar un constructor (el mas comun __init__)

# class dino () :
#     color = None
#     nombre = None

#     def __init__(self, nombre):
#         print("estoy en el constructor", nombre)
#         self.color = "verde"
#         self.nombre = nombre

#     def __delattr__(self):
#         print("estoy en el destructor",self.__class__)            #   el __class__ es para ponerle el nombre de la clase en la que esta

# R = dino ("Mallic")
# print(R.color+"1")
# print(R.nombre)

# del(R)                                                              #   con del() eliminas todas las referensias a esa variavle
# print(R.color)
# print(R.nombre)

# -------------------------------------------------constructor--------------------------------------------------------------------------------
# -------------------------------------------------constructor--------------------------------------------------------------------------------
# -------------------------------------------------constructor--------------------------------------------------------------------------------

#   los contructores solo se disparan si se instansias una clase



# class jugete():
#     _encendido = True

#     def __init__(self,x):
#         print("estoy en la clase jugete en su cnstructor(", x, ")")

#     def encendido(self):
#         print("encendiendo")
#         self._encendido = True

#     def apaga (self):
#         print ("apagando")
#         self._encendido = False

#     def isEncendido (self) :
#         return self._encendido

# class dino (jugete) :
#     color= None
#     nombre = None

#     def __init__ (self, nombre) :
#         # jugete.__init__(self)                                   #   asi se puede llamar a otro __init__ que se encuentra en una clase padre
#         # jugete.__init__(self, nombre)                           #   asi se llama el constructor si tuviera un parametro

#         # super().__init__()                                      #     esta forma es mas comun de hacer lo mismo super(). hace referensi a la clase padre
#         super().__init__(nombre)                                #     asi se llama el constructor si tuviera un parametro

#         print ("estoy en el constructor de la clase dino")

# P = dino("mi dinosaurio")
#------------------------------------------como imprimir con constructores---------------------------------------------------------------------
#------------------------------------------como imprimir con constructores---------------------------------------------------------------------
#------------------------------------------como imprimir con constructores---------------------------------------------------------------------

class Jugete:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

                        #   el metodo __str__ se usa para representar una salida informal para codigo de producsion
    def __str__(self):  #   sin el metodo __str__ no imprime informacion legible legible
        return f"el nmbre del jugete es {self.nombre} y el precio es {self.precio}" 

    #   el metodo __repr__ se usa para una salida mas tecnica para codigo en desarollo o deporasion
    def __repr__(self):
        return f" __repr__ nombre {self.nombre} precio {self.precio}"

j1 = Jugete ("autito", 10.5)
#   por defecto el print llama el metodo str
print (j1)
#   si en la clase tiene el modulo str y no el repr y se imboca repr se imprime el comportamento por defecto que es como si no tubiera str
print(repr(j1))

#------------------------------------------como imprimir con constructores---------------------------------------------------------------------
#------------------------------------------como imprimir con constructores---------------------------------------------------------------------
#------------------------------------------como imprimir con constructores---------------------------------------------------------------------

# __str__ es un método para definir una representación en cadena de un objeto.

# class Veiculo () :

#     def __init__ (self, color, ruedas, puertas) :
#         self.color = color
#         self.ruedas = ruedas
#         self.puertas = puertas

# class Coche (Veiculo) :
#     def __init__ (self, color, Velocidad, ruedas, puertas, cilindros) :
#         super().__init__(color, ruedas, puertas) 
#         self.Velocidad = Velocidad
#         self.cilindros = cilindros

#     def __str__(self):
#         return "color {}, km/h {}, ruedas {}, puertas {}, colindros {} ".format (self.color , self.Velocidad , self.ruedas ,self.puertas , self.cilindros)

# A = Coche ("rojo ", 100 , 4 , 5 , "v-8" )

# print (A)

#   Por ejemplo, si definimos una clase (Coche) y queremos que se imprima una cadena de objetos al llamar a la función print, podemos definir el método __str__ para la clase
#   para llamar un metodo __str__ se usa str()
#   para retornar un __str__ de una clase ya instansiada dentro de otra clase instanciada se usa (return str()) y despues el print

# ----------------------------clases abstractas------------------------------------------------------------------------------------------------
# ----------------------------clases abstractas------------------------------------------------------------------------------------------------
# ----------------------------clases abstractas------------------------------------------------------------------------------------------------

#   una clases abstractas sirve para definir un conjunto de funciones comunes a otras clases
#   las clases clases abstractas no se pueden instanciar
#   para instansiar un a clases abstractas se tiene que derivar

# from abc import ABC, abstractclassmethod

# class Animal (ABC) :
#     @abstractclassmethod                    #   el metodo que tenga ensima @abstractclassmethod esta obligado a
#     def sonido (self):                      #   defimirlo en todas las clases hijos
#         print ("animal")

#     def Di_Hola(self) :
#         print ("hola")

# class Perro (Animal):

#     def sonido (self) :
#         print ("GUAU,GUAU,GUAU,GUAU ")

# class Gato (Animal):

#     def sonido (self) :
#         print ("soy otro gato ")

# class Caballo (Animal) :

#     def sonido (self) :
#         print ("trabajo con jorge")

# P = Perro ()
# P.sonido ()
# P.Di_Hola ()

# G = Gato ()
# G.sonido ()
# G.Di_Hola ()

# C = Caballo ()
# C.sonido ()
# C.Di_Hola ()


#-------------------------------Clases compuestas------------------------------------------------------------------------------------
#-------------------------------Clases compuestas------------------------------------------------------------------------------------
#-------------------------------Clases compuestas------------------------------------------------------------------------------------
#   las clases compuestas van por orden de gerarquias mientras una clase llame a metodos dentro de otra clase 
#   esta va por devajo

# class Motor () :
#     tipo = "diesel"

# class Ruedas () :
#     cantidad = 4

# class Ventana () :
#     cantidad = 5

#     def cambiarcantidad (self, valor):
#         self.cantidad = valor 
# class Carroceria () :
#     ventana = Ventana ()
#     ruedas = Ruedas ()

# class Auto () :
#     motor = Motor ()
#     carroceria = Carroceria ()

# A = Auto ()
# print ("motor es ", A.motor.tipo)
# print ("ventanas", A.carroceria.ventana.cantidad)

# A.carroceria.ventana.cambiarcantidad(3)                 #   asi se resuelve una composision
# print ("ventanas", A.carroceria.ventana.cantidad)