from django.shortcuts import render

from .models import Director, Genero, Pelicula, Instancia_pelicula

def index (request) :
    Cantidad_de_peliculas = Pelicula.objects.all().count()
    Instancias_de_peliculas = Instancia_pelicula.objects.all().count()
    Cantidad_de_directores = Director.objects.all().count()
    Peliculas_disponivles = Instancia_pelicula.objects.filter (status__exact = "A").count()

    return render (
        request,
        "index.html",
        context = {
        "Cantidad_de_peliculas": Cantidad_de_peliculas,
        "Instancias_de_peliculas": Instancias_de_peliculas,
        "Cantidad_de_directores": Cantidad_de_directores,
        "Peliculas_disponivles": Peliculas_disponivles,
        }
    )