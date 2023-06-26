from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def menu_inicio (request:HttpRequest):
    return render (request, "menu/inicio/menu_inicio.html")