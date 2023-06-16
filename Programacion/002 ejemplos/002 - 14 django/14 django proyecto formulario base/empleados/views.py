from django.shortcuts import render
from .forms import EmpleadoForm, LocalForm, DepartamentoForm, PaisForm, TrabajoForm, SalarioForm
from .models import Pais,Departamento,Local,Salario,Trabajo,Empleado

def inicio (request) :
    return render (request, "menus/inicio/inicio.html", {})

def menu_crear(request):
    #   request.path.split("/")[1] toma la ruta con la que llamas a la funcion la corta por / y toma el elemento 1 y lo envia por el parametro al html
    ruta = request.path.split("/")[1]
    return render(request, "menus/menu_crear.html", {"ruta":ruta})

def menu_ver (request) :
    ruta = request.path.split("/")[1]
    return render(request, "menus/menu_ver.html", {"ruta":ruta})

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
    if request.method == "POST" and objeto_1.is_valid():
        objeto_1.save()

    return render(request, "acciones/crear.html", {"ver": objeto_2, "ruta":ruta})

def super_ver (request, resource, objeto_1, objeto_2, objeto_3, rutas) :
    rutas = request.path.split("/")
    ruta = rutas[1]+"/"+rutas[2]

    match rutas[2] :
        case "empleado" :
            return render (request, "acciones/ver_form/ver_empleado.html", {"ruta":ruta, 'objeto_3': objeto_3})
        case "local" :
            return render (request, "acciones/ver_form/ver_local.html", {"ruta":ruta, 'objeto_3': objeto_3})
        case "departamento" :
            return render (request, "acciones/ver_form/ver_departamento.html", {"ruta":ruta, 'objeto_3': objeto_3})
        case "pais" :
            return render (request, "acciones/ver_form/ver_pais.html", {"ruta":ruta, 'objeto_3': objeto_3})
        case "trabajo" :
            return render (request, "acciones/ver_form/ver_trabajo.html", {"ruta":ruta, 'objeto_3': objeto_3})
        case "salario" :
            return render (request, "acciones/ver_form/ver_salario.html", {"ruta":ruta, 'objeto_3': objeto_3})

def editar (request, resource, id) :
    rutas = request.path.split("/")

    match rutas[2] :
        case "empleado":
            relleno = Empleado.objects.get (id=id)

            if request.method == "POST":
                objeto_1 = EmpleadoForm (request.POST, instance=relleno)

                if objeto_1.is_valid():
                    objeto_1.save()

                    return empleado (request, resource)

            else:
                objeto_1 = EmpleadoForm (instance=relleno)

        case "local":
            relleno = Local.objects.get (id=id)

            if request.method == "POST":
                objeto_1 = LocalForm (request.POST, instance=relleno)

                if objeto_1.is_valid():
                    objeto_1.save()

                    return local (request, resource)

            else:
                objeto_1 = LocalForm (instance=relleno)

        case "departamento":
            relleno = Departamento.objects.get (id=id)

            if request.method == "POST":
                objeto_1 = DepartamentoForm (request.POST, instance=relleno)

                if objeto_1.is_valid():
                    objeto_1.save()

                    return departamento (request, resource)

            else:
                objeto_1 = DepartamentoForm (instance=relleno)

        case "pais":
            relleno = Pais.objects.get(id=id)

            if request.method == "POST":
                objeto_1 = PaisForm (request.POST, instance=relleno)

                if objeto_1.is_valid():
                    objeto_1.save()

                    return pais (request, resource)

            else:
                objeto_1 = PaisForm (instance=relleno)

        case "trabajo":
            relleno = Trabajo.objects.get(id=id)

            if request.method == "POST":
                objeto_1 = TrabajoForm (request.POST, instance=relleno)

                if objeto_1.is_valid():
                    objeto_1.save()

                    return trabajo (request, resource)

            else:
                objeto_1 = TrabajoForm (instance=relleno)

        case "salario":
            relleno = Salario.objects.get(id=id)

            if request.method == "POST":
                objeto_1 = SalarioForm (request.POST, instance=relleno)

                if objeto_1.is_valid():
                    objeto_1.save()

                    return salario (request, resource)

            else:
                objeto_1 = SalarioForm (instance=relleno)

    return render (request, "acciones/editar.html", {"ver": objeto_1})

def borrar (request, resource, id) :
    rutas = request.path.split("/")
    ruta = rutas[1]+"/"+rutas[2]

    match rutas[2] :
        case "empleado":
            relleno = Empleado.objects.get (id=id)
            objeto_1 = EmpleadoForm (instance=relleno)

            if request.method == "POST":
                relleno.delete()

                return empleado (request, resource)

        case "local":
            relleno = Local.objects.get (id=id)
            objeto_1 = LocalForm (instance=relleno)

            if request.method == "POST":
                relleno.delete()

                return local (request, resource)

        case "departamento":
            relleno = Departamento.objects.get (id=id)
            objeto_1 = DepartamentoForm (instance=relleno)

            if request.method == "POST":
                relleno.delete()

                return departamento (request, resource)

        case "pais":
            relleno = Pais.objects.get (id=id)
            objeto_1 = PaisForm (instance=relleno)

            if request.method == "POST":
                relleno.delete()

                return pais (request, resource)

        case "trabajo":
            relleno = Trabajo.objects.get (id=id)
            objeto_1 = TrabajoForm (instance=relleno)

            if request.method == "POST":
                relleno.delete()

                return trabajo (request, resource)

        case "salario":
            relleno = Salario.objects.get (id=id)
            objeto_1 = SalarioForm (instance=relleno)

            if request.method == "POST":
                relleno.delete()

                return salario (request, resource)

    return render (request, "acciones/borrar.html", {"ver":objeto_1, "ruta":ruta})

def relaciones (request, resource, id):
    empleado = Empleado.objects.get(id=id)
    trabajo = empleado.trabajo
    salario = trabajo.salario
    local = empleado.local
    departamento = local.departamento
    pais = departamento.pais

    return render (request, "acciones/ver_relaciones/relacion_empleado.html", { 
    "empleado" : empleado,
    "trabajo" : trabajo,
    "salario" : salario,
    "local" : local,
    "departamento" : departamento,
    "pais" :  pais,})






