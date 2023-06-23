from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def inicio (request:HttpRequest):
    return HttpResponse ("app tareas")