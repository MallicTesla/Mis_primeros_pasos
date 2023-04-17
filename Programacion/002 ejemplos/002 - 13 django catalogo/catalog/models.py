from django.db import models
from django.urls import reverse
import uuid

# aca se crean los modelos

class Genre (models.Model) :
    name = models.CharField (max_length = 64, help_text = "nombre del genero")      
    #   CharField es un campo de tipo caracter con la longitut maxima de 64 caracteres (max_length = 64)
    #   (help_text = "nombre del genero") cuando entremos a administrasion se va a ver el texto

    #   se crea un "override" se refiere a la acción de redefinir un método o atributo en una subclase para personalizar su comportamiento.

    def __str__ (self) :
        return self.name

class Book (models.Model) :
    # django genera el id automaticamente se puede espesificar que tipo de ide queres que sea
    title = models.CharField (max_length = 32)
    # se crea una calbe foranea que hace referencia a otra tabla (author)
    # on_delete = models.SET_NULL, null = True es para que cuando se borra un un autor de la tabla (author) es numero sea null (inexistente)
    # y null = True es para que el campo author pueda tener un balor null
    # todo esto es para que puedas mantener la integridad referencial 
    author = models.ForeignKey ("author", on_delete = models.SET_NULL, null = True)
    # TextField se un campo en el que se pueden agregar mas caracteres que con CharField
    summary = models.TextField (max_length = 100, help_text = "porn aqui de que va el libro")
    isbn = models.CharField ("ISBN", max_length = 13, help_text = "el ISBN de 13 caracteres")
    # ManyToManyField es para relasionar es para que (book) pueda estar relasionado con barios (Genre)
    genre = models.ManyToManyField (Genre)

    def __str__(self) :
        return self.title

    def get_absolute_url (self) :
        return reverse ("book-detail", args = [str (self.id)])

class BookInstance (models.Model) :
    # UUIDField genera un codigo aleatorio que es extremadamente improbable que se repita en el mundo (en este caso se usa para la id) 
    id = models.UUIDField (primary_key = True, default = uuid.uuid4, help_text = "ide unico para este libro")
    book = models.ForeignKey ("Book", on_delete = models.SET_NULL, null = True)
    imprint = models.CharField (max_length = 200)
    # es para asignarle un estado al libro
    due_back = models.DateField (null = True, blank = True)

    # es una lista para asignarle un estado al los libros 
    LOAN_STATUS = (
    ("m", "Maintenence"),
    ("o", "On loan"),
    ("a", "Available"),
    ("r", "Reserced"),
    )

    # es para elegir en que estadoe esta el libro
    # max_length = 1 es para que eliga el primer valor de la lista que esta en el dicsionario
    # choices = LOAN_STATUS se pasa un dicsionario con las distintas opsiones 
    # blank = True se permite que no tenga ningun estado , default = "m" estado por defecto es m 
    status = models.CharField (max_length = 1, choices = LOAN_STATUS, blank = True, default = "m", help_text = "Disponibilidad del libro")

    class Mate : 
        ordering = ["due_back"]

    def __str__(self) :
        return "%s (%s)" % (self.id, self.book.title)

class Author (models.Model) :
    first_name = models.CharField (max_length = 100)
    last_name = models.CharField (max_length = 100)
    date_of_birth = models.DateField (null = True, blank = True)
    date_of_death = models.DateField (null = True, blank = True)

    def get_absolute_url (self) :
        return reverse ("author-detail", args = [str(self.id)])
    
    def __str__(self) :
        return "%s (%s)" % (self.last_name, self.first_name)
