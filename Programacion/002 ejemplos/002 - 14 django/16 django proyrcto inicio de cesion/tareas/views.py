from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
#   para manejar errores en la base de datos
from django.db import IntegrityError

#   esto debuelve un formulario ya echo para crear un usuario, crea un formulario para inisiar sesion
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#   para guardar un usuario
from django.contrib.auth.models import User
#   crea una cooki con el usuario, lo ciera y lo autentifica
from django.contrib.auth import login, logout, authenticate
#   da la fecha y la hora
from django.utils import timezone
#   inporta un decorador para proteger las funsiones para que no ingresen
#   ahi que agregarle algo en setings
from django.contrib.auth.decorators import login_required

from .forms import TareaForm
from .models import Tarea

def menu (request:HttpRequest):
    return render (request, "texto_menu.html", {})

def registro (request:HttpRequest):
    mensaje = ""

    if request.method == "GET":
        print ("enviando formulario")

    else:
        #   para ver si la confirmasion de la contntraseña es corecta
        if request.POST["password1"] == request.POST["password2"]:
            #   la creasion de un usuario se coloca dentro de un try por si se crean 2 usuarios con el mismo nombre
            try:
                #   user es un objeto que contiene el usuario con la contraseña a guardar
                user = User.objects.create_user(username = request.POST["username"], password = request.POST["password1"])
                #   guarda el usuaario en la base de datos 
                user.save()
                # mensaje = "Usuario creado"
                login (request, user)
                return redirect ("tareas")

            except IntegrityError:
                #   este except es por si existe otro usuario con el mismo nombre
                mensaje = "El usuario ya existe"

        else:
            mensaje = "Las contraseñas no son iguales"

        print (request.POST)
        print ("obtenienfo datos")

    return render (request, "registro_form.html", {'form':UserCreationForm, "mensaje":mensaje})

@login_required
def tareas (request:HttpRequest):
    #   asi busco las tareas de un usuario solamente
    objeto_1 = Tarea.objects.filter(usuario = request.user)

    return render (request, "tareas.html", {"tareas":objeto_1})

def salir (request:HttpRequest):
    logout (request)
    return redirect ("menu")

def iniciar_sesion (request:HttpRequest):
    mensaje = ""
    if request.method == "POST":
        #   para autntificar el usuario
        user = authenticate (request, username=request.POST["username"], password=request.POST["password"])
        if user is None :
            mensaje = "usuario o contraseña incorecta"

        else:
            #   inisia la sesion con las credensiales y te redirige a otra pagina
            login (request, user)
            return redirect ("tareas")

    return render (request, "iniciar_sesion.html", {"form":AuthenticationForm, "mensaje":mensaje})

@login_required
def crear_tarea (request:HttpRequest) :
    objeto_1 = TareaForm (request.POST)
    objeto_2 = TareaForm ()

    if request.method == "POST" and objeto_1.is_valid():
        #   para rellenar el campo usuario de forma automatica se hace asi
        #   ases un falso guardado y al resultado lo guardas en una variavle
        guardar = objeto_1.save(commit = False)
        #   despues completas ese campo faltante con el nombre del campo y la riquest corespondiente y despues se guarda
        guardar.usuario = request.user
        guardar.save()

    return render (request, "crear_tareas.html", {"form":objeto_2})

@login_required
def tarea (request:HttpRequest, tarea_id):
    tarea_1 = Tarea.objects.get (id = tarea_id)

    #   esto es para evitar que un usuario entre a las tareas de otro usuario
    if tarea_1.usuario != request.user:
        return redirect ("tareas")

    if request.method == "POST":
        #   crea el formulario relleno para editarlo
        objeto_1 = TareaForm (instance=tarea_1)
        #   unaves editado este otro objeto lo guarda
        objeto_2 = TareaForm (request.POST, instance=tarea_1)

        if objeto_2.is_valid():
            guardar = objeto_2.save(commit = False)
            guardar.usuario = request.user
            guardar.save()

        else:
            return render (request, "crear_tareas.html", {"form":objeto_1})

    return render (request, "tarea.html", {"tarea":tarea_1})

def tarea_completa (request:HttpRequest, tarea_id):
    tarea = get_object_or_404 (Tarea, pk = tarea_id, usuario=request.user)

    if request.method == "POST":
        tarea.fecha_finalisaddo = timezone.now()
        tarea.save()

    return redirect ("tareas")

@login_required
def borar_tarea (request:HttpRequest, tarea_id):
    tarea = get_object_or_404 (Tarea, pk = tarea_id, usuario=request.user)

    if request.method == "POST":
        tarea.delete()

    return redirect ("tareas")




