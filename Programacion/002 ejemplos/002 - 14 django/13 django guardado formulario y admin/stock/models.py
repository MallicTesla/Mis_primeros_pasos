from django.db import models
from datetime import date

class Producto (models.Model) :
    nombre = models.CharField (max_length = 50, blank = False, null = False)
    vreve_descripcion = models.CharField (max_length = 100, blank = False, null = False)
    descripcion = models.TextField (blank = False, null = False)
    stock = models.IntegerField (default = 20)
    descuento_asta = models.DateField(default = date.today)

    def __str__(self) :
        return self.nombre
