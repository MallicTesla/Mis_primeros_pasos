from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
#   esto debuelve un formulario ya echo
from django.contrib.auth.forms import UserCreationForm
#   para guardar un usuario
from django.contrib.auth.models import User

def menu (request:HttpRequest):
    return render (request, "menu.html", {})

def registro (request:HttpRequest):
    if request.method == "GET":
        print ("enviando formulario")

    else:
        #   para ver si la confirmasion de la contntraseña es corecta
        if request.POST["password1"] == request.POST["password2"]:
            #   registrar usuario
            User.objects.create_user(username = request.POST["use"])

        return HttpRequest ("las contraseñas no son iguales")

        print (request.POST)
        print ("obtenienfo datos")

    return render (request, "registro_form.html", {'form':UserCreationForm})




