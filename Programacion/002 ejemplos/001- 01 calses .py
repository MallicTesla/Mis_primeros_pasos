#---------------------clase dinamica----------------------
class dino:
    _encendido = "primera variavle "        #   esto es un metodo "si tiene un _ no se deveria manipular fuera de la clase"

    def apagado(self):                      #   esto es un metodo
        self._encendido = False             #   el self. se usa para hacerle refencia a la variavle dentro de la clase

    def encendido (self):
        self._encendido = False

d1 = dino()                                 #   instanciar una clase contiene todos los metodos de la clas
d2 = dino()                                 #   antes de poder llamar un metodo primero ahi que instansear la clase

print(d1._encendido)
print(d1._encendido + "1")

d1._encendido = "hola"                      #   el . se usa para llamar un metodo dentro de una clase
print(d1._encendido)

d1.apagado()
print(d1._encendido)