from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import ContactoForm, GrupoForm, Relacionar_Contacto_GrupoForm
from .models import Contacto, Grupo

def inicio (request:HttpRequest):
    return render (request, "menu/contactos/menu.html")

def crear_contacto (request:HttpRequest):
    objeto_1 = ContactoForm (request.POST)
    objeto_2 = ContactoForm ()

    if request.method == "POST" and objeto_1.is_valid():
        objeto_1.save()

    return render (request, "contactos/form_contacto.html", {"ver": objeto_2})

def crear_grupo (request:HttpRequest):
    objeto_1 = GrupoForm (request.POST)
    objeto_2 = GrupoForm ()

    if request.method == "POST" and objeto_1.is_valid():
        objeto_1.save()

    return render (request, "contactos/form_grupo.html", {"ver": objeto_2})

def relacionar_contacto_grupo (request:HttpRequest):
    objeto_1 = Relacionar_Contacto_GrupoForm(request.POST)
    objeto_2 = Relacionar_Contacto_GrupoForm()

    if request.method == "POST" and objeto_1.is_valid():
        #   crea una instancia del campo contacto
        contacto = objeto_1.cleaned_data ["contacto"]
        grupo = objeto_1.cleaned_data ["grupo"]
        #   asi se guarda la relacion 
        contacto.grupo_set.add(grupo)

    return render (request, "contactos/relacionar_contacto_grupo.html", {"ver": objeto_2})

def ver_contacto (request:HttpRequest):
    objecto_1 = Contacto.objects.all()

    return render (request, "contactos/ver_contactos.html", {"ver": objecto_1})