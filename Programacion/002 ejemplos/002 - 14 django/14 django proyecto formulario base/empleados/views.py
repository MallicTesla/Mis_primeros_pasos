from django.shortcuts import render
from .forms import EmpleadoForm, LocalForm, DepartamentoForm, PaisForm, TrabajoForm, SalarioForm

def inicio (request) :
    return render (request, "inicio.html", {})

def menu (request) :
    return render (request, "menu_crear.html", {})

def crear (request) :
    return render (request, "crear.html", {})

def empleado (request) :
    if request.method == "POST" :
        empleado = EmpleadoForm (request.POST)

        if empleado.is_valid :
            #   asi se guarda el modelo
            empleado.save ()
            return render (request, "crear.html", {"ver":empleado, "request": request})

    else :
        empleado = EmpleadoForm ()
        return render (request, "crear.html", {"ver":empleado, "request": request})

    return render (request, "crear.html", {"ver":empleado, "request": request})

def local (request) :
    if request.method == "POST" :
        local = LocalForm (request.POST)

        if local.is_valid :
            #   asi se guarda el modelo
            local.save ()
            return render (request, "crear.html", {"ver":local, "request": request})

    else :
        local = LocalForm ()
        return render (request, "crear.html", {"ver":local, "request": request})

    return render (request, "crear.html", {"ver":local, "request": request})

def departamento(request):
    if request.method == "POST":
        departamento = DepartamentoForm(request.POST)
        
        if departamento.is_valid():
            departamento.save()
            return render(request, "crear.html", {"ver": departamento, "request": request})
    else:
        departamento = DepartamentoForm()
    
    return render(request, "crear.html", {"ver": departamento, "request": request})

def pais(request):
    if request.method == "POST":
        pais = PaisForm(request.POST)
        
        if pais.is_valid():
            pais.save()
            return render(request, "crear.html", {"ver": pais, "request": request})
    else:
        pais = PaisForm()
    
    return render(request, "crear.html", {"ver": pais, "request": request})

def trabajo(request):
    if request.method == "POST":
        trabajo = TrabajoForm(request.POST)
        
        if trabajo.is_valid():
            trabajo.save()
            return render(request, "crear.html", {"ver": trabajo, "request": request})
    else:
        trabajo = TrabajoForm()
    
    return render(request, "crear.html", {"ver": trabajo, "request": request})

def salario(request):
    if request.method == "POST":
        salario = SalarioForm(request.POST)
        
        if salario.is_valid():
            salario.save()
            return render(request, "crear.html", {"ver": salario, "request": request})
    else:
        salario = SalarioForm()
    
    return render(request, "crear.html", {"ver": salario, "request": request})
