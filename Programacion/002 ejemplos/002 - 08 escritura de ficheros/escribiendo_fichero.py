# f = open ("C:\Pruevas\hola-copia.txt", "w")     #   asi re escrivis el mismo fichero

# f.write ("datos1\n")
# f.write("datos2\n")

# f = open ("C:\Pruevas\hola-copia.txt", "a")     #   asi agregas al mismo fichero

# f.write("datos1\n")
# f.write("datos2\n")

# f = open ("C:\Pruevas\hola-copia.txt", "w")     #   asi re escrivis el mismo fichero

#-------------------una forma de guardar una lista en un fichero linia por linia-----------------------------------------------------------

# def escribe (direcsion,datos):
#     f = open (direcsion,"w")

#     for linea in datos:
#         if not linea.endswith("\n"):
#             linea = linea + "\n"

#         f.write (linea)

#     f.close()

# lista = ["1linia","2linia","3linia"]

# escribe ("C:\Pruevas\hola-copia.txt",lista)

#--------------------------------------------------modulo pickle------------------------------------------------------------
#   sirve para serealisar datos y deserealisar datos
#   significa que podes guardar datos (ojetos) de un programa y despues leerlos

import pickle

class jugete :
    nombre = ""
    precio = 0.0

    def __init__(self,nombre,precio) :
        self.nombre = nombre
        self.precio = precio

    def getNombre (self) :
        return self.nombre

# j1 = jugete ("autito",10.06)                    #   desactivado para llamar a el fichero

# print (type(j1))
# print (j1.getNombre())

#-------------------asi se guarda--------------------------------------------------------

# f = open ("C:\Pruevas\clase.txt", "wb")         #   sovre escrive un fichero en binario
# pickle.dump (j1, f)                             #   con la funcion .dump(que quiero guardar, donde lo quiero guardar) guardo el fichero
# f.close

#----------------------asi se lee---------------------------------------------------

f = open ("C:\Pruevas\clase.txt", "rb")         #   lee un archibo en binario
auto = pickle.load(f)                           #   con la funcion .load(direcsion del fichero) se lee un fichero
f.close

print (type(auto))
print ("nombre", auto.getNombre(),"precio", auto.precio)











