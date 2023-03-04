import pickle

class jugete :
    nombre = ""
    precio = 0.0

    def __init__(self,nombre,precio) :
        self.nombre = nombre
        self.precio = precio

j1 = jugete ("autito",10.06)

f = open ("C:\Pruevas\Ejercicio11clase.txt", "wb")
pickle.dump (j1, f)
f.close

print ("se termina de guardar y comiensa la lectura")

f = open ("C:\Pruevas\clase.txt", "rb") 
auto = pickle.load(f)
f.close

print ("Nombre", auto.nombre, "precio", auto.precio)