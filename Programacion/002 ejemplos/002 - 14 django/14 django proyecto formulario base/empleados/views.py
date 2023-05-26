from django.shortcuts import render
from .forms import EmpleadoForm, LocalForm, DepartamentoForm, PaisForm, TrabajoForm, SalarioForm
from .models import Pais,Departamento,Local,Salario,Trabajo,Empleado

def inicio (request) :
    return render (request, "inicio.html", {})

def menu_crear(request):
    #   request.path.split("/")[1] toma la ruta con la que llamas a la funcion la corta por / y toma el elemento 1 y lo envia por el parametro al html
    ruta = request.path.split("/")[1]
    return render(request, "menu_crear.html", {"ruta":ruta})

def menu_ver (request) :
    ruta = request.path.split("/")[1]
    return render(request, "menu_ver.html", {"ruta":ruta})

def super_creasion (request, resource, objeto_1, objeto_2, ruta) :
    if request.method == "POST":
        if objeto_1.is_valid():
            objeto_1.save()

    elif request.method == "PUT":
        return render(request, "crear.html", {"ver": objeto_2, "request": request, "resource": resource, "ruta":ruta})

    return render(request, "crear.html", {"ver": objeto_2, "request": request, "resource": resource, "ruta":ruta})

def salario (request, resource) :
    """
    cuando se llama a este mentodo crea 2 objetos diferentes y lo debuelve 
    """
    objeto_1 = SalarioForm(request.POST)
    objeto_2 = SalarioForm ()
    ruta = request.path.split("/")[1]
    return super_creasion (request, resource, objeto_1, objeto_2, ruta)

def trabajo (request, resource) :
    objeto_1 = TrabajoForm (request.POST)
    objeto_2 = TrabajoForm ()
    ruta = request.path.split("/")[1]
    return super_creasion (request, resource, objeto_1, objeto_2, ruta)
    
def pais (request, resource) :
    objeto_1 = PaisForm (request.POST)
    objeto_2 = PaisForm ()
    ruta = request.path.split("/")[1]
    return super_creasion (request, resource, objeto_1, objeto_2, ruta)

def departamento (request, resource) :
    objeto_1 = DepartamentoForm (request.POST)
    objeto_2 = DepartamentoForm ()
    ruta = request.path.split("/")[1]
    return super_creasion (request, resource, objeto_1, objeto_2, ruta)

def local (request, resource) :
    objeto_1 = LocalForm (request.POST)
    objeto_2 = LocalForm ()
    ruta = request.path.split("/")[1]
    return super_creasion (request, resource, objeto_1, objeto_2, ruta)

def empleado (request, resource) :
    objeto_1 = EmpleadoForm (request.POST)
    objeto_2 = EmpleadoForm ()
    ruta = request.path.split("/")[1]
    return super_creasion (request, resource, objeto_1, objeto_2, ruta)
