from django.shortcuts import render
from .forms import EmpleadoForm, LocalForm, DepartamentoForm, PaisForm, TrabajoForm, SalarioForm

def inicio (request) :
    return render (request, "inicio.html", {})

def menu (request) :
    return render (request, "menu_crear.html", {})

def menu_crear (request) :
    return render (request, "crear.html", {})

def super_creasion (request, objeto_1, objeto_2) :
    if request.method == "POST":
        if objeto_1.is_valid():
            objeto_1.save()
            # return render(request, "crear.html", {"ver": objeto_1, "request": request})

    return render(request, "crear.html", {"ver": objeto_2, "request": request})

def salario (request) :
    objeto_1 = SalarioForm(request.POST)
    objeto_2 = SalarioForm ()
    return super_creasion (request, objeto_1, objeto_2)

def trabajo (request) :
    objeto_1 = TrabajoForm (request.POST)
    objeto_2 = TrabajoForm ()
    return super_creasion (request, objeto_1, objeto_2)
    
def pais (request) :
    objeto_1 = PaisForm (request.POST)
    objeto_2 = PaisForm ()
    return super_creasion (request, objeto_1, objeto_2)

def departamento (request) :
    objeto_1 = DepartamentoForm (request.POST)
    objeto_2 = DepartamentoForm ()
    return super_creasion (request, objeto_1, objeto_2)

def local (request) :
    objeto_1 = LocalForm (request.POST)
    objeto_2 = LocalForm ()
    return super_creasion (request, objeto_1, objeto_2)

def empleado (request) :
    objeto_1 = EmpleadoForm (request.POST)
    objeto_2 = EmpleadoForm ()
    return super_creasion (request, objeto_1, objeto_2)