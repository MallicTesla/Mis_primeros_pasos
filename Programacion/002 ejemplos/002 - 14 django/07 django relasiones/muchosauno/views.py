from django.shortcuts import render
from django.http import HttpResponse
from .models import Reportero, Articulo
from datetime import date

def crear (request) :
    rep = Reportero (nombre = "mallic", apellido = "Tesla", email = "MallicTesla@hotmail.com")
    rep.save ()

    art1 = Articulo (titulo = "primer articulo", fecha = date (2023,1,11), reportero =rep)
    art1.save ()
    art2 = Articulo (titulo = "segundo articulo", fecha = date (2023,1,20), reportero =rep)
    art2.save ()
    art3 = Articulo (titulo = "tersero articulo", fecha = date (2023,1,30), reportero =rep)
    art3.save ()
    art4 = Articulo (titulo = "cuarto articulo", fecha = date (2023,1,15), reportero =rep)
    art4.save ()
    art5 = Articulo (titulo = "quinto articulo", fecha = date (2023,1,18), reportero =rep)
    art5.save ()

    resultado1 = art1.reportero.nombre
    #   para llamar a todos los articulos relasionados con el reportero se hace asi se coloca la el ovjeto (rep) 
    #   punto la otra clase en minuscual (articulo) y alfinal se agrega _set
    #   punto se ase la consulta
    resultado2 = rep.articulo_set.all()

    return HttpResponse (resultado2 )
