from django.db import models
from datetime import date

class Autor (models.Model) :
    nombre = models.CharField (max_length = 200)
    email = models.EmailField ()

    def __str__(self) :
        return self.nombre

class Entrada (models.Model) :
    #   asi se hace una clabe frania en django 
    #   para que no se rompa todo cuando se borra un autor se usa on_delete = models.CASCADE que bora todas las entradas de ese autor
    autor = models.ForeignKey (Autor, on_delete = models.CASCADE)
    titulo = models.CharField (max_length = 255)
    cuerpo_texto = models.TextField ()
    #   la fecha por defecto es la de la puvlicasion
    fecha_publicasion = models.DateField (default = date.today)
    reiting = models.IntegerField (default = 5)

    def __str__(self) :
        return self.titulo
