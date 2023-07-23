from django.shortcuts import render
from django.http import HttpRequest
#   llama a la app de mensajes
from django.contrib import messages

def mensaje (request:HttpRequest):
    # messages.success
    messages.success (request, "Este mensaje funciono")

    return render (request, "mensajes.html", {})
