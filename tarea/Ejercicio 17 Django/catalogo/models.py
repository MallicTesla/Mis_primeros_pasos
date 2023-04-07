from django.db import models
from django.urls import reverse
import uuid

class Genero (models.Model) :
    nombre = models.CharField (max_length = 64, help_text = "nombre del genero")      

    def __str__ (self) :
        return self.nombre

class Pelicula (models.Model) :
    titulo = models.CharField (max_length = 32)
    director = models.ForeignKey("catalogo.Director", on_delete=models.SET_NULL, null=True)
    resumen = models.TextField (max_length = 100, help_text = "Brebe descripsin de la pelicula")
    isbn = models.CharField ("ISBN", max_length = 13, help_text = "el ISBN de 13 caracteres")
    genero = models.ManyToManyField (Genero)

    def __str__(self) :
        return self.titulo

    def get_absolute_url (self) :
        return reverse ("Detales-de-pelicula", args = [str (self.id)])

class Instancia_pelicula (models.Model) : 
    id = models.UUIDField (primary_key = True, default = uuid.uuid4, help_text = "ide unico para este libro")
    pelicula = models.ForeignKey ("Pelicula", on_delete = models.SET_NULL, null = True)
    imprint = models.CharField (max_length = 200)
    estado_de_la_pelicula = models.DateField (null = True, blank = True)

    ESTADOS = (
    ("M", "Mantenimiento"),
    ("P", "Prestado"),
    ("D", "Disponible"),
    ("R", "Reservado"),
    )

    status = models.CharField (max_length = 1, choices = ESTADOS, blank = True, default = "M", help_text = "Disponibilidad del pelicula")

    class Mate : 
        ordering = ["estado_de_la_pelicula"]

    def __str__(self) :
        return "%s (%s)" % (self.id, self.pelicula.titulo)

class Director (models.Model) :
    primer_nombre = models.CharField (max_length = 100)
    apellido = models.CharField (max_length = 100)
    fecha_nacimiento = models.DateField (null = True, blank = True)
    fecha_defuncion = models.DateField (null = True, blank = True)

    def get_absolute_url (self) :
        return reverse ("Detalles del director", args = [str(self.id)])
    
    def __str__(self) :
        return "%s (%s)" % (self.apellido, self.primer_nombre)