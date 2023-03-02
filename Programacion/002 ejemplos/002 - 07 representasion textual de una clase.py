# numero = 15
# texto = "ola ke ase"
# otro_mas = 1.

# print(type(numero))
# numtex = str (numero)           #   asi de cambia un tipo de variable a otra (de int a str)
# print (type(numtex))

# print (repr(numero))
# print (numtex)

# class Jugete:
#     nombre = ""
#     precio = 0.0

#     def __init__(self, nombre, precio):
#         self.nombre = nombre
#         self.precio = precio

#                         #   el metodo __str__ se usa para representar una salida informal para codigo de producsion
#     def __str__(self):  #   sin el metodo __str__ no imprime informacion legible legible
#         return f"el nmbre del jugete es {self.nombre} y el precio es {self.precio}" 

#     #   el metodo __repr__ se usa para una salida mas tecnica para codigo en desarollo o deporasion
#     def __repr__(self):
#         return f"nombre {self.nombre} precio {self.precio}"

# j1 = Jugete ("autito", 10.5)
# #   por defecto el print llama el metodo str
# print (j1)
# #   si en la clase tiene el modulo str y no el repr se imboca repr se imprime el comportamento por defecto que es como si no tubiera str
# print(repr(j1))

# import pprint

cadena = "en un lugar de la manchA"

# pprint.pprint(dir(cadena)) #    dir mestra la propiedades de un objeto 

print (cadena)
print (cadena.capitalize())         #   pone en mayuscula la primera letra del texto y las demas en minuscula
print (cadena.title())              #   pone en mayuscula la primera letra de cada palabra y el resto en minuscula
print (cadena.count("a"))           #   cuenta cuantas veses aparese una letra en el texto (diferensia entre minuscula y mayuscula)
print (cadena.lower())              #   combierte todo a minuscula
print (cadena.upper())              #   combierte todo a mayuscula

print (cadena.lower().count("a"))
# esto seria lo mismo
otra_cadena = cadena.lower()
print (otra_cadena.count("a"))

print (cadena.split())              #   combierte una cadena en una lista, cambia lo que esta dentro de los parentesis por un espacio en blanco con una coma (", ")

cadena1 = "     con espasios el prinsipio y finaL       "

print (cadena1)
print (cadena1.strip())             #   elimina los espasios al principio y al final
print (cadena1.lstrip())            #   elimina los espasios al principio
print (cadena1.rstrip())            #   elimina los espasios al final



# numero = "55"
# alfa = "Hola"
# alfnumerico = "a1"

# print (numero.isdigit())                #   te dice si el strin esta compuesto solo por numeros
# print (alfa.isalpha())                  #   te dice si el strin esta compuesto solo por letras
# print (alfnumerico.isalnum())           #   te dice si el strin esta compuesto por numeros, letras o ambos



