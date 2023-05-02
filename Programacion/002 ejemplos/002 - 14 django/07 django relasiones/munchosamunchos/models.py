from django.db import models

class Publicasion (models.Model) :
    titulo = models.CharField (max_length = 30)

    def __str__ (self) :
        return self.titulo

class Articulo (models.Model) :
    linia = models.CharField (max_length = 100)
    #   para relasionar una relasion de muchos a munchos se utilisa ManyToManyField (el nombre de la ortra clase a relasionar) 
    publicasiones = models.ManyToManyField (Publicasion)

    def __str__ (self) :
        return self.linia



