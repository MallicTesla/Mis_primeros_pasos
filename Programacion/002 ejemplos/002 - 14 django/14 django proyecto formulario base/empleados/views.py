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

def salario (request, resource) :
    """
    cuando se llama a este mentodo crea 2 objetos diferentes y lo debuelve 
    """
    objeto_1 = SalarioForm(request.POST)
    objeto_2 = SalarioForm ()
    objeto_3 = Salario.objects.all()
    rutas = request.path.split("/")
    return separar_rutas (request, resource, objeto_1, objeto_2, objeto_3, rutas)

def trabajo (request, resource) :
    objeto_1 = TrabajoForm (request.POST)
    objeto_2 = TrabajoForm ()
    objeto_3 = Trabajo.objects.all()
    rutas = request.path.split("/")
    return separar_rutas (request, resource, objeto_1, objeto_2, objeto_3, rutas)
    
def pais (request, resource) :
    objeto_1 = PaisForm (request.POST)
    objeto_2 = PaisForm ()
    objeto_3 = Pais.objects.all()
    rutas = request.path.split("/")
    return separar_rutas (request, resource, objeto_1, objeto_2, objeto_3, rutas)

def departamento (request, resource) :
    objeto_1 = DepartamentoForm (request.POST)
    objeto_2 = DepartamentoForm ()
    objeto_3 = Departamento.objects.all()
    rutas = request.path.split("/")
    return separar_rutas (request, resource, objeto_1, objeto_2, objeto_3, rutas)

def local (request, resource) :
    objeto_1 = LocalForm (request.POST)
    objeto_2 = LocalForm ()
    objeto_3 = Local.objects.all()
    rutas = request.path.split("/")
    return separar_rutas (request, resource, objeto_1, objeto_2, objeto_3, rutas)

def empleado (request, resource) :
    objeto_1 = EmpleadoForm (request.POST)
    objeto_2 = EmpleadoForm ()
    objeto_3 = Empleado.objects.all()
    rutas = request.path.split("/")
    return separar_rutas (request, resource, objeto_1, objeto_2, objeto_3, rutas)

def separar_rutas (request, resource, objeto_1, objeto_2, objeto_3, rutas):
    ruta = rutas[1]
    if ruta == "menu_crear" :
        return super_creasion (request, resource, objeto_1, objeto_2, objeto_3, ruta)

    elif ruta == "menu_ver" :
        return super_ver (request, resource, objeto_1, objeto_2, objeto_3, rutas)

def super_creasion (request, resource, objeto_1, objeto_2, objeto_3, ruta) :
    if request.method == "POST" or objeto_1.is_valid():
        objeto_1.save()

    elif request.method == "POST":
        return render(request, "crear.html", {"ver": objeto_2, "request": request, "ruta":ruta})

    return render(request, "crear.html", {"ver": objeto_2, "request": request, "ruta":ruta})

def super_ver (request, resource, objeto_1, objeto_2, objeto_3, rutas) :
    ruta = rutas[1]
    match rutas[2] :
        case "empleado" :
            return render(request, "ver_form/ver_empleado.html", {"request": request, "ruta":ruta, 'objeto_3': objeto_3})
        case "local" :
            return render(request, "ver_form/ver_local.html", {"request": request, "ruta":ruta, 'objeto_3': objeto_3})
        case "departamento" :
            return render(request, "ver_form/ver_departamento.html", {"request": request, "ruta":ruta, 'objeto_3': objeto_3})
        case "pais" :
            return render(request, "ver_form/ver_pais.html", {"request": request, "ruta":ruta, 'objeto_3': objeto_3})
        case "trabajo" :
            return render(request, "ver_form/ver_trabajo.html", {"request": request, "ruta":ruta, 'objeto_3': objeto_3})
        case "salario" :
            return render(request, "ver_form/ver_salario.html", {"request": request, "ruta":ruta, 'objeto_3': objeto_3})




