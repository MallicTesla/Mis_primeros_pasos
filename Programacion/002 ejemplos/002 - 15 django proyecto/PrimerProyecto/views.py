from django.shortcuts import render

def inisio (request) :
    return render (request, "inicio.html", {})

def donde_vivo (request) :
    return render (request, "donde_vivo.html", {})

def futuro (request) :
    return render (request, "futuro.html", {})