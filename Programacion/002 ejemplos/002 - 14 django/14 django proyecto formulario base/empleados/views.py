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

def super_creasion (request, resource, objeto_1, objeto_2, objeto_3, ruta) :
    if ruta == "menu_crear" :
        if request.method == "POST" or objeto_1.is_valid():
            objeto_1.save()

        elif request.method == "POST":
            return render(request, "crear.html", {"ver": objeto_2, "request": request, "resource": resource, "ruta":ruta})

        return render(request, "crear.html", {"ver": objeto_2, "request": request, "resource": resource, "ruta":ruta})

    elif ruta == "menu_ver" :
        # if request.method == "POST" or objeto_1.is_valid():
        #     objeto_1.save()

        # elif request.method == "POST":
        #     return render(request, "ver_form/ver_empleado.html", {"ver": objeto_2, "request": request, "resource": resource, "ruta":ruta, 'objeto_3': objeto_3})

        return render(request, "ver_form/ver_empleado.html", {"ver": objeto_2, "request": request, "resource": resource, "ruta":ruta, 'objeto_3': objeto_3})

def salario (request, resource) :
    """
    cuando se llama a este mentodo crea 2 objetos diferentes y lo debuelve 
    """
    objeto_1 = SalarioForm(request.POST)
    objeto_2 = SalarioForm ()
    objeto_3 = Salario.objects.all()
    ruta = request.path.split("/")[1]
    return super_creasion (request, resource, objeto_1, objeto_2, objeto_3, ruta)

def trabajo (request, resource) :
    objeto_1 = TrabajoForm (request.POST)
    objeto_2 = TrabajoForm ()
    objeto_3 = Trabajo.objects.all()
    ruta = request.path.split("/")[1]
    return super_creasion (request, resource, objeto_1, objeto_2, objeto_3, ruta)
    
def pais (request, resource) :
    objeto_1 = PaisForm (request.POST)
    objeto_2 = PaisForm ()
    objeto_3 = Pais.objects.all()
    ruta = request.path.split("/")[1]
    return super_creasion (request, resource, objeto_1, objeto_2, objeto_3, ruta)

def departamento (request, resource) :
    objeto_1 = DepartamentoForm (request.POST)
    objeto_2 = DepartamentoForm ()
    objeto_3 = Departamento.objects.all()
    ruta = request.path.split("/")[1]
    return super_creasion (request, resource, objeto_1, objeto_2, objeto_3, ruta)

def local (request, resource) :
    objeto_1 = LocalForm (request.POST)
    objeto_2 = LocalForm ()
    objeto_3 = Local.objects.all()
    ruta = request.path.split("/")[1]
    return super_creasion (request, resource, objeto_1, objeto_2, objeto_3, ruta)

def empleado (request, resource) :
    objeto_1 = EmpleadoForm (request.POST)
    objeto_2 = EmpleadoForm ()
    objeto_3 = Empleado.objects.all()
    ruta = request.path.split("/")[1]
    return super_creasion (request, resource, objeto_1, objeto_2, objeto_3, ruta)
    




