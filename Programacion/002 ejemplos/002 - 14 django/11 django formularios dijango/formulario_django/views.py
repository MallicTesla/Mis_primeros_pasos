from django.http import HttpResponse
from django.shortcuts import render
#   se importa el archivo forms
from .forms import Comentario
def form (request) :
    #   ais se aparese la caja de texto rellena por defecto. si aui un initial lo anula 
    comentario_formulario = Comentario ({"nambre":"Pablo", "url":"www.mallic.com", "comentario":"esto va a funcionar"})
    #   asi queda el formulario como esta en el archivo forms
    # comentario_formulario = Comentario
    return render (request, "form.html", {"comentario_formulario":comentario_formulario})

def contenido (request) :
    if request.method != "POST" :
        return HttpResponse ("metodo no permitido")

    return HttpResponse (request.POST["nambre"])
