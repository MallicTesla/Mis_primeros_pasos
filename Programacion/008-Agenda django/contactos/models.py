from django.db import models
from datetime import date

class Contacto (models.Model):
    nombre = models.CharField (max_length = 30, null = False, blank = False)
    apellido = models.CharField (max_length = 30, null = True, blank = True)
    cel = models.CharField (max_length = 15, null = False, blank = False)
    tel = models.CharField (max_length = 15, null = True, blank = True)
    email = models.EmailField ()
    trabajo = models.CharField (max_length = 30, null = True, blank = True)
    nota = models.TextField (blank = True, null = True)
    fecha_registro = models.DateField (default = date.today)

    def __str__(self):
        return self.nombre, self.apellido

class Grupo (models.Model):
    nombre = models.CharField (max_length= 20, null = False, blank = False)
    contactos = models.ManyToManyField (Contacto, blank=True)

    def __str__(self):
        return self.nombre