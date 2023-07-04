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

def ver_tareas (request:HttpRequest):
    tareas = Tarea.objects.all ()

    return render (request, "tarea/ver_tareas.html", {"tareas":tareas})

            # <li><h4><a href="{% url 'contactos:borrar_contacto' id_contacto=contacto.id%}" class="boton">Borrar contacto</a></h4></li>
            # <li><h4><a href="{% url 'contactos:borrar_contacto' id_contacto=contacto.id%}" class="boton">Borrar contacto</a></h4></li>