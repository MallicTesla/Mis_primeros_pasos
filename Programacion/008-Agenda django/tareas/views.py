from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Tarea
from .forms import TareaForm

def inicio (request:HttpRequest):
    return render (request, "menu/tareas/menu.html", {})

def crear_tarea (request:HttpRequest):
    objeto_1 = TareaForm (request.POST)
    objeto_2 = TareaForm ()

    if request.method == "POST" and objeto_1.is_valid():
        objeto_1.save()

    return render (request, "tarea/form_tarea.html", {"ver": objeto_2})

def ver_tareas (request:HttpRequest, letter=None):
    if letter != None:
        tareas = Tarea.objects.filter (titulo__istartswith = letter)

    else:
        tareas = Tarea.objects.filter (titulo__icontains = request.GET.get ("buscar", ""))

    return render (request, "tarea/ver_tareas.html", {"tareas":tareas})

def borrar_tarea (request:HttpRequest, id_tarea):
    tarea = Tarea.objects.get (id = id_tarea)

    tarea.delete()

    return (ver_tareas(request))

def editar_tarea (request:HttpRequest, id_tarea):
    relleno = Tarea.objects.get (id=id_tarea)

    if request.method == "POST":
        objeto_1 = TareaForm (request.POST, instance=relleno)

        if objeto_1.is_valid():
            objeto_1.save()

            return (ver_tareas(request))

    else:
        objeto_1 = TareaForm (instance=relleno)

    return render (request, "tarea/form_tarea.html", {"ver": objeto_1})
