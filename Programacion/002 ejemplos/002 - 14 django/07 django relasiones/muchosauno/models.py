from django.db import models

class Reportero (models.Model) :
    nombre = models.CharField (max_length = 30)
    apellido = models.CharField (max_length = 30)
    email = models.EmailField ()

    def __str__ (self) :
        return self.email

#   ya que un articulo puede tener solo un creador (reportero) la clave forania va en el articulo
class Articulo (models.Model) :
    titulo = models.CharField (max_length = 100)
    fecha = models.DateField ()
    #   cuando se crea una relasion normalmente se creea con el mismo nombre de la clase 
    #   cuando se usa el modulo ForeignKey (se le tiene que pasar primero el nombre de la clase con la que se le quiere relasionar
    #   , que es lo que ocure cuando se borra un dato, y como se va a realisar la relasion)
    reportero = models.ForeignKey (Reportero, on_delete = models.CASCADE)

    def __str__(self) :
        return self.titulo