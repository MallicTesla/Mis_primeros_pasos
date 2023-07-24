from django.shortcuts import render
from django.http import HttpRequest
from .models import Producto

def filtro (request:HttpRequest, letra ):
    #   el doble gion __ es para buscar en ese campo despues viene que tiene que buscar (en este caso busca la primera letra y no tiene encuenta tildes malluscula y minuscula)
    productos = Producto.objects.filter (nombre__istartswith = letra)

    return render (request, "filtros.html", {"productos":productos})
