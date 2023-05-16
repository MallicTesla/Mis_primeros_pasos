from django.shortcuts import render
from django.http import HttpResponse

def form (request) :
    
    return render (request, "form.html", {})

def destino (request) :
    #   esto es una extroctura de guarda
    if request.method != "GET" :
        return HttpResponse ("el metodo POST no esta soportado")

    nombre = request.GET["nombre"]


    return render (request, "suseso.html", {"nombre": nombre})
