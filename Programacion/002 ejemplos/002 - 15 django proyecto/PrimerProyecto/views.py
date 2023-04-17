from django.shortcuts import render

def inisio (request) :
    return render (request, "inicio.py", {})

def perfil (request) :
    return render (request, "perfil.py", {})

def trabajos (request) :
    return render (request, "trabajos.py", {})