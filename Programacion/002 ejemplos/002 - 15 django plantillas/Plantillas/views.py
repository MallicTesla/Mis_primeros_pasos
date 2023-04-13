from django.shortcuts import render
#   render es para renderisar el archivo html

def simple (request) :
    #   para retornar el archivo html se coloca render (request, "simple.html (simple.html es el archivo si estuviera en otra carpeta se colocaria
    #   la direcsion primero)", {aca va el contexto y se entrega como disionario} )
    return render (request,"simple.html", {} )