from django.shortcuts import render
from django.http import HttpResponse
from . models import Comment

def test (request) :
    return HttpResponse ("Funciono")

def crear (request) :
    # #   asi creo un registro en la base de datos
    # comentario = Comment (name = "Pablo", score = 5, comment = "Este es un comentario")
    # #   y asi se guarda el registro
    # comentario.save ()

    # tambien se puede hacer asi se crea y guarda el objeto
    comentario = Comment.objects.create (name = "Mallic", score = 4, comment = "Este es otro comentario")

    return HttpResponse ("Ruta para probar la creacion de modelos y guardar datos en la base de datos")
