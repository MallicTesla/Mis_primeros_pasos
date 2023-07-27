class Matematica ():
    #   metodo
    def suma (self):
        self.n1 = 2
        self.n2 = 3

s = Matematica ()
s.suma ()

print (s.n1 + s.n2)

# ---------------------------------------------------------------

class Ropa () :
    #   constructor 
    #   lo que se encuentra dentro de la funsion __init__ se ejecuta automaticamente cuando se lla la clase
    def __init__(self) :
        self.marca = "Wilson"
        self.talla = "M"
        self.color = "rojo"

camis = Ropa ()

print (camis.talla)
print (camis.marca)

# ------------------------------------

class Calculadora () :
    def __init__ (self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.multiplicar = n1 * n2
        self.dividir = n1 / n2

operacion = Calculadora (2, 3)
print (operacion.multiplicar)
print (operacion.suma)
