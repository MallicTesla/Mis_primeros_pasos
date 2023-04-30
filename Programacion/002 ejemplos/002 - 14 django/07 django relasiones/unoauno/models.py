from django.db import models

class Lugar (models.Model) :
    nombre = models.CharField (max_length = 50)
    direcsion = models.CharField (max_length = 80)

    def __str__(self) :
        return self.nombre

class Restaurante (models.Model) :
    #   cuando se crea una relasion normalmente se creea ek mismo nombre de la clase 
    #   cuando se usa el modulo de relasionamiento OneToOneField (se le tiene que pasar primero el nombre de la clase con la que se le quiere relasionar
    #   , que es lo que ocure cuando se borra un dato, y como se va a realisar la relasion)
    lugar = models.OneToOneField (Lugar, on_delete = models.CASCADE, primary_key = True)
    numero_empleados = models.IntegerField (default = 1 )

    def __str__(self) :
        return self.lugar.nombre