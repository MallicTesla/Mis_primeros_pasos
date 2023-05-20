from django.db import models

class Empleado (models.Model) :
    nombre = models.CharField (max_length = 50, blank = False, null = False)
    apellido = models.CharField (max_length = 50, blank = False, null = False)
    email = models.EmailField (max_length = 50, blank = False, null = False)

    def __str__(self) :
        return self.nombre