from django.db import models
from datetime import date

class Tarea (models.Model) :
    titulo = models.CharField (max_length = 30, null = False, blank = False)
    breve_descripcion = models.CharField (max_length = 50, null = True, blank = True)
    descripcion = models.TextField (null = True, blank = True)
    fecha_registro = models.DateField (default = date.today)

    def __str__(self):
        return self.titulo
