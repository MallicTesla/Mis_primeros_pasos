from django.shortcuts import render

from .models import Director, Genero, Pelicula, Instancia_pelicula

def index (request) :
    Cantidad_de_peliculas = Pelicula.objects.all().count()
    Instansias_de_peliculas = Instancia_pelicula.objects.all().count()
    Cantidad_de_directores = Director.objects.all().count()
    Peliculas_disponivles = Instancia_pelicula.objects.filter (status__exact = "A").count()

    return render (
        request,
        "index.html",
        context = {
        "Cantidad de peliculas": Cantidad_de_peliculas,
        "Instansias de peliculas": Instansias_de_peliculas,
        "Cantidad de directores": Cantidad_de_directores,
        "Peliculas disponivles": Peliculas_disponivles,
        }
    )