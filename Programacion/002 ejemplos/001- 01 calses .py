#---------------------clase dinamica----------------------
class dino:
    _encendido = True                       #   esto es un metodo "si tiene un _ no se deveria manipular fuera de la clase"

    def apagado(self):                      #   esto es un metodo
        self._encendido = False             #   el self. se usa para hacerle refencia a la variavle dentro de la clase

    def apagado (self):
        self._encendido = False


d1 = dino()                                 #   instanciar una clase contiene todos los metodos de la clase
d1.apagado()                                #   el . se usa para llamar un metodo dentro de una clase
print(d1._encendido)