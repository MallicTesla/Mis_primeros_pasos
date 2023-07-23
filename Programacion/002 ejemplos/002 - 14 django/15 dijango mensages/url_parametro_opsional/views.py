from django.shortcuts import render
from django.http import HttpRequest

#   cuando tenes una url con variavle opcional tenes que darle un valor por defectp a la varoavle
def opcional (request:HttpRequest, nombre="Nombre por defecto"):

    return render (request, "opcional.html", {"nombre": nombre})

