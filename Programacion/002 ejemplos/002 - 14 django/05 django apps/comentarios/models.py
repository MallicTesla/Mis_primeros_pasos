from django.db import models

#   despues de crear o modificar cada modelo (clases) se ejecuta el comando python manage.py makemigrations para ver los cambios u despues se migran para guardarlos

class Comment (models.Model) :

    name = models.CharField (max_length = 255, null = False)
    score = models.IntegerField (default = 3)
    comment = models.TextField (max_length = 1000, null = True)
    fecha = models.DateField (null = True)
    #   si se agrega un campo (columna) nuevo a un codigo existente ay que espesiicar si es null o agregarle un valor por defecto
    asignatura = models.CharField (max_length = 100, default = "Fiema")


    def __str__ (self) :
        return self.name