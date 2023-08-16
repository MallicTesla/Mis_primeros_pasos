from django.db import models
#   para poder relasionar tablas a un usuario se importa User
from django.contrib.auth.models import User

class Tarea (models.Model):
    titulo = models.CharField (max_length=100)
    descripsion = models.TextField (blank = True)
    creado = models.DateTimeField (auto_now_add= True)
    fecha_finalisaddo = models.DateTimeField(null = True)
    importansia = models.BooleanField (default = False)
    #   relasiona la tabla Usuarios con esta
    usuario = models.ForeignKey (User, on_delete = models.CASCADE)

    def __str__(self):
        #   loque esta aca se ve en el panel de administracion
        #   con self.usuario.username se agrega el nombre del usuario de la tabla user
        return self.titulo + " echo por " + self.usuario.username
