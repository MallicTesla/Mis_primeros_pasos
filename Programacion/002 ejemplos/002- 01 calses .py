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

# #---------------------------calse estatica-------------------------------------------
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


# ---------------------------------calase eredada-----------------------------
#   las clases eradadas se usan para no repetir el mismo codigo dentro de otras clases
#   y la clase que se desea eredar se coloca dentro de los parentesis de las clases

class usuaria () :
    
    def ocupante (self):
        self.nombre = input ("nombre : ")
        self.apellido = input ("apellido : ")
    
    def estadia (self):
        self.dias = int (input ("cuantos dias te quedas : "))

class cuarto_01 (usuaria) :
    _cuarto = "Cuarto 01"

    def cama (self) :
        self.plazas = int (input ("plasas de la cama : "))
        self.color = input ("color_de_la_cama : ")
    def baño (self) :
        self.ducha = "si"

class cuarto_02 (usuaria) :
    _cuarto = "cuarto 02 "

    def cama (self) :
        self.plazas = int (input ("plasas de la cama : "))
        self.color = input ("color_de_la_cama : ")

    def baño (self) :
        self.ducha = "no"

A_01 = cuarto_01 ()
A_01.ocupante ()
A_01.estadia ()
A_01.cama ()
A_01.baño ()

print( A_01._cuarto,"ocupante", A_01.nombre, A_01.apellido ,"dias",A_01.dias,"caracteristicas de la cama( plazas",A_01.plazas,"color",A_01.color,")")

A_02 = cuarto_02 ()
A_02.ocupante ()
A_02.estadia ()
A_02.cama ()
A_02.baño ()

print( A_02._cuarto,"ocupante", A_02.nombre, A_02.apellido ,"dias",A_02.dias,"caracteristicas de la cama( plazas",A_02.plazas,"color",A_02.color,")")
