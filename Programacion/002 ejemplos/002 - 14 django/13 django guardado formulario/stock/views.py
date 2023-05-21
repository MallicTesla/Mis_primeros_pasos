from django.shortcuts import render
from .forms import ProductoForm

def inicio (request) :
    if request.method == "POST" :
        formulario = ProductoForm (request.POST)
        if formulario.is_valid :
            #   asi se guarda el modelo
            formulario.save ()
            return render (request, "inicio.html", {"formulario":formulario})
    else :
        formulario = ProductoForm ()
        return render (request, "inicio.html", {"formulario":formulario})
