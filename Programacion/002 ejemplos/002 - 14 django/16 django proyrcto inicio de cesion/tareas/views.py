from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
#   para manejar errores en la base de datos
from django.db import IntegrityError

#   esto debuelve un formulario ya echo para crear un usuario
from django.contrib.auth.forms import UserCreationForm
#   para guardar un usuario
from django.contrib.auth.models import User
#   crea una cooki con el usuario
from django.contrib.auth import login

def menu (request:HttpRequest):
    return render (request, "menu.html", {})

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

def tareas (request:HttpRequest):
    
    return render (request, "tareas.html", {})


