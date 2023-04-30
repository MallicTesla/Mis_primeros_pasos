from django.shortcuts import render
from django.http import HttpResponse
from .models import Lugar, Restaurante

def crear (request) :
    lugar = Lugar (nombre = "Lugar 1", direcsion = "Calle demo")
    lugar.save ()

    restaurante = Restaurante (lugar = lugar, numero_empleados = 8)
    restaurante.save ()
    return HttpResponse (restaurante.lugar.nombre)

