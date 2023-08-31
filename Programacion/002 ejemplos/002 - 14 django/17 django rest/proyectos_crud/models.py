from django.db import models

class Proyecto (models.Model):
    titulo = models.CharField (max_length=200)
    descripsion = models.TextField ()
    tecnologia = models.CharField (max_length=200)
    agregado = models.DateTimeField (auto_now_add=True)

