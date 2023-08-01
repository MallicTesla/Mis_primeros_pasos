# class Torta :
#     def __init__(self, ingredientes) :
#         self.ingredientes = ingredientes

#     def __repr__(self) -> str:
#         return f"Torta ({self.ingredientes !r})"

#     @classmethod
#     def Torta_chocolate (cls) :
#         return cls(["harina","leche","chocolate"])
    
#     @classmethod
#     def Toorta_vainilla (cls):
#         return cls(["harina","leche","vainilla"])

# print (Torta.Torta_chocolate())

# ----------------------------------------------------------
import math

class Torta :
    def __init__(self, ingredientes, tamaño) :
        self.ingredientes = ingredientes
        self.tamaño = tamaño
    
    def __repr__(self) :
        return (f"torta({self.ingredientes}, "f"{self.tamaño})")
    
    def area (self):
        return self.tamaño_area(self.tamaño)

    #   este decorador hace que el metodo sea un metodo estatico lo que significa que no está asociado a una instancia particular de la clase y no requiere self 
    @staticmethod
    def tamaño_area (a):
        return a ** 2 * math.pi

nueva_torta = Torta (["hariana","azucar","leche","crema"],4)

print (nueva_torta.ingredientes)
print (nueva_torta.tamaño)

print (nueva_torta.area())

print (nueva_torta.tamaño_area (12))
