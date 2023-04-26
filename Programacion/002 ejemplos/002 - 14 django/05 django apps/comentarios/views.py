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

def borrar (request) :
    #   para borrar contenido de la base de datos se crea un objeto que busque un contenido en la base de datos con .get
    # comentraio = Comment.objects.get (id = 1)
    # comentraio.delete ()

    #   tambien se puede hacer asi utilisando filter (espesificando el parametro)
    Comment.objects.filter (id = 4).delete ()
    return HttpResponse ("Borrando datos de la base de datos")
