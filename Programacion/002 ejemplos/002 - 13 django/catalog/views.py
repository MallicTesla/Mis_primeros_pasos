from django.shortcuts import render

#   se importan los modelos 
from .models import Author, Genre, Book, BookInstance

# se crea la funcion index

def index (request) :
    #   se optiene el numero de libros
    num_books = Book.objects.all().count()
    #   se optiene el numero de instancias
    num_inctances = BookInstance.objects.all().count()
    #   se optiene el numero de authores
    num_authors = Author.objects.all().count()

    #   para ver los libros disponivles
    #   aca se trabaja con la base de datos
    #   status__exact = "a" es para que los campos sean exactamente igual a la letra "a" y con count te da la cantidad de libros con ese campo
    disponivles = BookInstance.objects.filter (status__exact = "a").count()

#   request hace referencia a el parametro de la funcion 
#   despues se hace referensia al archivo de la plantilla html que va a mostrar el contenido luego en context van los datos que resive el archibo html
    return render (
        request,
        "index.html",
        context = {
        "num_books": num_books,
        "num_inctances": num_inctances,
        "num_authors": num_authors,
        "disponivles": disponivles,
        }
        
    )
