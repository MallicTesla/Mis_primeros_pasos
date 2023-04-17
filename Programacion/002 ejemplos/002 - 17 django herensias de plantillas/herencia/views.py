from django.shortcuts import render

def index (request) :
    return render (request, "index.html", {})

def herencia (request) :
    return render (request, "herencia.html", {})

def ejemplo (request) :
    return render (request, "ejemplo.html", {})

def otro (request) :
    return render (request, "otro.html", {})