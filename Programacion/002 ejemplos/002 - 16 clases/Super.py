#   la funsion super se usa para llamar a metodos ya definidos prinsipalmente se uasa en clases con herensias en la clase segundarias

class Mamfero:
    def __init__(self,nombre):
        print (nombre, "es un animal de sangre caliente")

class Leon (Mamfero):
    def __init__(self):
        print ("el leon es un animal carnivoro")
        super().__init__ ("Tiger")
        #   el super es lo mismo que esto
        # Mamfero.__init__(self,"Tiger")

nuevo_leon = Leon()