from django.http import HttpResponse
from django.shortcuts import render
#   se importa el archivo forms
from .forms import Comentario
def form (request) :
    comentario_formulario = Comentario
    return render (request, "form.html", {"comentario_formulario":comentario_formulario})

def contenido (request) :
    if request.method != "POST" :
        return HttpResponse ("metodo no permitido")

    return HttpResponse (request.POST["nambre"])
