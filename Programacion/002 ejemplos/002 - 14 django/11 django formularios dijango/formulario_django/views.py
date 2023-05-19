from django.http import HttpResponse
from django.shortcuts import render
#   se importa el archivo forms
from .forms import Comentario,ContactoForm

def form (request) :
    #   ais se aparese la caja de texto rellena por defecto. si aui un initial lo anula 
    comentario_formulario = Comentario ({"nombre":"Pablo", "url":"www.mallic.com", "comentario":"esto va a funcionar"})
    #   asi queda el formulario como esta en el archivo forms
    # comentario_formulario = Comentario
    return render (request, "form.html", {"comentario_formulario":comentario_formulario})

def contenido (request) :
    if request.method != "POST" :
        return HttpResponse ("metodo no permitido")

    return HttpResponse (request.POST["nombre"])

def widget (request) :
    if request.method == "GET":
        contacto = ContactoForm
        return render (request, "widget.html", {"contacto":contacto})

    if request.method == "POST" :
        contacto = ContactoForm (request.POST)
        #   ocure esto cuando todos los datos son corectos
        if contacto.is_valid () :
            return HttpResponse ("POST vlido")
        #   ocure esto cuando todos los datos no son corectos
        else :
            return render (request, "widget.html", {"contacto":contacto})