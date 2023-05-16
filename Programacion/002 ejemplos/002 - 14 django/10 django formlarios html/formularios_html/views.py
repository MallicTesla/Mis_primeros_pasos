from django.shortcuts import render
from django.http import HttpResponse

def getform (request) :
    
    return render (request, "form.html", {})

def getdestino (request) :
    #   esto es una extroctura de guarda
    if request.method != "GET" :
        return HttpResponse ("el metodo POST no esta soportado")

    nombre = request.GET["nombre"]

    return render (request, "suseso.html", {"nombre": nombre})

def postform (request) :
    return render (request, "postform.html", {})

def postdestino (request) :
    if request.method != "POST" :
        return HttpResponse ("el metodo POST no esta soportado")

    nombre = request.POST["nombre"]

    return render (request, "suseso.html", {"nombre": nombre})
