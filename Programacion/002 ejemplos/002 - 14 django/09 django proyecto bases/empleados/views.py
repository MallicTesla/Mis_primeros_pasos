from django.shortcuts import render
from django.http import HttpResponse
from .models import Pais,Departamento,Local,Salario,Trabajo,Empleado

def crear (request) :
    pais1 = Pais (nombre = "Uruguay")
    pais1.save ()
    pais2 = Pais (nombre = "Italia")
    pais2.save ()

    departamento1 = Departamento (departamento = "Montevideo")
    departamento1.save ()
    departamento2 = Departamento (departamento = "Milan")
    departamento2.save ()

    local1 = Local (local_nombre = "Piedras Blancas", direccion = "te rovan esquina el negro maicol")
    local1.save ()
    local2 = Local (local_nombre = "Bella italia", direccion = "31 de febrero esquina lola")
    local2.save ()
    local3 = Local (local_nombre = "vaprio da adda", direccion = "puevlo de miera alado del rio")
    local3.save ()
    local4 = Local (local_nombre = "Pero", direccion = "donde vive el marce serca del shoping")
    local4.save ()

    salario1 = Salario ()
    salario1.save ()
    salario2 = Salario (monto_anual = 20000)
    salario2.save ()
    salario3 = Salario (monto_anual = 25000, extra_junio = False, extra_nobiembre = False)
    salario3.save ()

    trabajo1 = Trabajo (titulo = "Peon", descripsion = "trabajar como negro")
    trabajo1.save ()
    trabajo2 = Trabajo (titulo = "Programaddor", descripsion = "trabajar como negro")
    trabajo2.save ()
    trabajo3 = Trabajo (titulo = "Traider", descripsion = "estresarse mientras operas y el reto del tiempo disfrutando")
    trabajo3.save ()
    trabajo4 = Trabajo (titulo = "Vivir del estado", descripsion = "tomar vino en la esquina y no hacer nada")
    trabajo4.save ()

    empleado1 = Empleado (nombre = "Pablo", apellido = "Mallic", ci = "666666/6", direccion = "calle falsa 1234", email = "el_mallic@hotmail.com")
    empleado1.save ()
    empleado2 = Empleado (nombre = "Franco", apellido = "Franquito", ci = "568723/1", direccion = "calle esonia 3214", email = "el_franco@hotmail.com")
    empleado2.save ()
    empleado3 = Empleado (nombre = "German", apellido = "Zakrue", ci = "666665/6", direccion = "donde esta la zapateria 1234", email = "Hombre_aleman@hotmail.com")
    empleado3.save ()
    empleado4 = Empleado (nombre = "Marcelo", apellido = "Mike", ci = "6543125/6", direccion = "en su casa 1234", email = "el_mike@hotmail.com")
    empleado4.save ()
    empleado5 = Empleado (nombre = "Jorge", apellido = "El Omat", ci = "658514565/6", direccion = "en su casa 1234", email = "el_yoomat@hotmail.com")
    empleado5.save ()
    empleado6 = Empleado (nombre = "Marcelo", apellido = "Mike", ci = "666666/6", direccion = "en su casa 1234", email = "el_mallic@hotmail.com")
    empleado6.save ()
    empleado7 = Empleado (nombre = "Matias", apellido = "Duke", ci = "666666/6", direccion = "alado de la plaza", email = "el_mon@hotmail.com")
    empleado7.save ()

    return HttpResponse ("base pronta")

def relacionamientos (request) :
    



    return HttpResponse ("Relasionamientos echos")