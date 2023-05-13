from django.shortcuts import render
from django.http import HttpResponse
from .models import Pais,Departamento,Local,Salario,Trabajo,Empleado

def crear (request) :
    #   asi no se duplica el contenido si ya fue creeado 
    pais1, created = Pais.objects.get_or_create (nombre = "Uruguay")#D1
    pais2, created = Pais.objects.get_or_create(nombre = "Italia")#D2
    pais3, created = Pais.objects.get_or_create (nombre = "donde vivo")#D3

    departamento1, created = Departamento.objects.get_or_create (departamento = "Montevideo")#L2 D1
    departamento2, created = Departamento.objects.get_or_create (departamento = "Milan")#L3 L4 D2
    departamento3, created = Departamento.objects.get_or_create (departamento = "donde vivo")#L1 D3

    local1, created = Local.objects.get_or_create (local_nombre = "En casa", direccion = "en la calle de enfrente")#L1 E1 E2
    local2, created = Local.objects.get_or_create (local_nombre = "Bella italia", direccion = "31 de febrero esquina lola")#L2 E3 E7
    local3, created = Local.objects.get_or_create (local_nombre = "vaprio da adda", direccion = "puevlo de miera alado del rio")#L3 E4
    local4, created = Local.objects.get_or_create (local_nombre = "Pero", direccion = "donde vive el marce serca del shoping")#L4 E5 E6

    #   cuando creeas un registro con los balores por defecto para evitar que se duplique se le pasa el id
    salario1, created = Salario.objects.get_or_create (id = 1)#T1 T4
    salario2, created = Salario.objects.get_or_create (monto_anual = 20000)#T2
    salario3, created = Salario.objects.get_or_create (monto_anual = 25000, extra_junio = False, extra_nobiembre = False)#T3

    trabajo1, created = Trabajo.objects.get_or_create (titulo = "Peon", descripsion = "trabajar como negro")# T1 / E3 E7
    trabajo2, created = Trabajo.objects.get_or_create (titulo = "Programaddor", descripsion = "trabajar como negro")#T2 / E2 E4
    trabajo3, created = Trabajo.objects.get_or_create (titulo = "Traider", descripsion = "estresarse mientras operas y el reto del tiempo disfrutando") #T3 / E1
    trabajo4, created = Trabajo.objects.get_or_create (titulo = "Vivir del estado", descripsion = "tomar vino en la esquina y no hacer nada")#T4 / E5 E6

    empleado1, created = Empleado.objects.get_or_create (nombre = "Pablo", apellido = "Mallic", ci = "666666/6", direccion = "calle falsa 1234", email = "el_mallic@hotmail.com")#E1
    empleado2, created = Empleado.objects.get_or_create (nombre = "Franco", apellido = "Franquito", ci = "568723/1", direccion = "calle esonia 3214", email = "el_franco@hotmail.com")#E2
    empleado3, created = Empleado.objects.get_or_create (nombre = "German", apellido = "Zakrue", ci = "666665/6", direccion = "donde esta la zapateria 1234", email = "Hombre_aleman@hotmail.com")#E3
    empleado4, created = Empleado.objects.get_or_create (nombre = "Marcelo", apellido = "Mike", ci = "6543125/6", direccion = "en su casa 1234", email = "el_mike@hotmail.com")#E4
    empleado5, created = Empleado.objects.get_or_create (nombre = "Jorge", apellido = "El Omat", ci = "658514565/6", direccion = "en su casa 1234", email = "el_yoomat@hotmail.com")#E5
    empleado6, created = Empleado.objects.get_or_create (nombre = "ale", apellido = "toledo", ci = "666666/6", direccion = "en su casa 1234", email = "el_mallic@hotmail.com")#E6
    empleado7, created = Empleado.objects.get_or_create (nombre = "Matias", apellido = "Duke", ci = "666666/6", direccion = "alado de la plaza", email = "el_mon@hotmail.com")# E7

    local1.departamento.add (departamento3)
    local2.departamento.add (departamento1)
    local3.departamento.add (departamento2)
    local4.departamento.add (departamento2)

    departamento1.ciudad.add (pais1)
    departamento2.ciudad.add (pais2)
    departamento3.ciudad.add (pais3)

    trabajo1.salario.add (salario1)
    trabajo2.salario.add (salario2)
    trabajo3.salario.add (salario3)
    trabajo4.salario.add (salario1)

    empleado1.trabajo.add (trabajo3)
    empleado1.local.add (local1)

    empleado2.trabajo.add (trabajo2)
    empleado2.local.add (local1)

    empleado3.trabajo.add (trabajo1)
    empleado3.local.add (local3)

    empleado4.trabajo.add (trabajo2)
    empleado4.local.add (local4)

    empleado5.trabajo.add (trabajo4)
    empleado5.local.add (local4)

    empleado6.trabajo.add (trabajo4)
    empleado6.local.add (local4)

    empleado7.trabajo.add (trabajo1)
    empleado7.local.add (local2)

    #asi no se hace
    # empleado1.trabajo.add (trabajo3)
    # trabajo3.salario.add (salario3)
    # empleado1.local.add (local1)
    # local1.departamento.add (departamento1)
    # departamento1.ciudad.add (pais1)

    # empleado2.trabajo.add (trabajo2)
    # trabajo2.salario.add (salario2)
    # empleado2.local.add (local1)
    # local1.departamento.add (departamento2)
    # departamento2.ciudad.add (pais2)

    # empleado3.trabajo.add (trabajo4)
    # trabajo3.salario.add (salario1)
    # empleado3.local.add (local2)
    # local2.departamento.add (departamento1)
    # departamento1.ciudad.add (pais1)

    return HttpResponse ("se crearon los registros")

def contenido (request) :

    empleado = Empleado.objects.get (nombre = "German")
    trabajo = empleado.trabajo.first ()
    salario = trabajo.salario.first ()
    local = empleado.local.first ()
    departamento = local.departamento.first ()
    pais = departamento.ciudad.first ()

    info = ("\nEMPLEADO",
            "\nnombre : ",empleado.nombre, 
            "\napellido : ", empleado.apellido,
            "\nci : ", empleado.ci, 
            "\ndiresion : ", empleado.direccion, 
            "\nemail : ", empleado.email,
            "\n",
            "\nTRABAJO",
            "\ntrabajo : ",trabajo.titulo, 
            "\ndescripsion : ",trabajo.descripsion,
            "\n",
            "\nSALARIO", 
            "\nsalario : ",salario.monto_anual, 
            "\nextra junio : ",salario.extra_junio, 
            "\nextra nobiembre :",salario.extra_nobiembre,
            "\n",
            "\nLOCAL",
            "\nnombre del local : ",local.local_nombre,
            "\ndireccion : ", local.direccion,
            "\n",
            "\nDEPARTAMENTO",
            "\ndepartamento : ",departamento.departamento,
            "\n",
            "\nPais",
            "\npais : ", pais.nombre,
            )

    return HttpResponse (info, content_type='text/plain')


def mostrar (request, elegido) :
    empleado = Empleado.objects.get (nombre = elegido)
    trabajo = empleado.trabajo.first ()
    salario = trabajo.salario.first ()
    local = empleado.local.first ()
    departamento = local.departamento.first ()
    pais = departamento.ciudad.first ()

    return render (request, "mostrar.html", { 
    "empleado" : empleado,

    "trabajo" : trabajo,

    "salario" : salario,

    "local" : local,

    "departamento" : departamento,

    "pais" :  pais,})

    # return render (request, "inicio.html", { 
    # "nombre" : empleado.nombre, 
    # "apellido" : empleado.apellido,
    # "ci" : empleado.ci, 
    # "diresion" : empleado.direccion, 
    # "email" : empleado.email,

    # "trabajo" : trabajo.titulo, 
    # "descripsion" : trabajo.descripsion,

    # "salario" : salario.monto_anual, 
    # "extra junio" : salario.extra_junio, 
    # "nextra nobiembre" : salario.extra_nobiembre,

    # "nombre del local" : local.local_nombre,
    # "direccion" : local.direccion,

    # "departamento" : departamento.departamento,

    # "pais" :  pais.nombre,})