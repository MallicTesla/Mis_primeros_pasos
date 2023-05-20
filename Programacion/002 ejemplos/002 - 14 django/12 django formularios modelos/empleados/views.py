from django.shortcuts import render
from django.http import HttpResponse
#   para mostrar un formulario con modelos se importa la calse del formulario
from .forms import EmpladosForm

def inicio (request) :
    form = EmpladosForm ()
    return render (request, "inicio.html", {"form": form })