from django.shortcuts import render

def inisio (request) :
    return render (request, "inicio.html", {})

def perfil (request) :
    return render (request, "perfil.html", {})

def trabajos (request) :
    return render (request, "trabajos.html", {})