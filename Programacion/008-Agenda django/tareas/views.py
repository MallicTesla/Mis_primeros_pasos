from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def inicio (request:HttpRequest):
    return render (request, "menu/tareas/menu.html", {})

def crear_tarea (request:HttpRequest):
    return