class Veiculo () :
    
    def __init__ (self, color, ruedas, puertas) :
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche (Veiculo) :
    def __init__ (self, color, ruedas, puertas, Velocidad,cilindros) :
        super().__init__(color, ruedas, puertas)
        self.Velocidad = Velocidad
        self.cilindros = cilindros

A = Coche ("rojo ",4 ,5 ,"elcansa 100km/h ", "V-8 ")

print("Color:", A.color)
print("Ruedas:", A.ruedas)
print("Puertas:", A.puertas)
print("Velocidad:", A.Velocidad)
print("Cilindrada:", A.cilindros)