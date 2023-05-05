from django.db import models

class Pais (models.Model) :
    nombre = models.CharField (max_length = 30)

class Departamento (models.Model) :
    departamento = models.CharField (max_length = 30)

    ciudad = models.ManyToManyField (Pais)

class Local (models.Model) :
    local_nombre = models.CharField (max_length = 50)
    direccion = models.CharField (max_length = 50)

    departamento = models.ManyToManyField (Departamento)

class Salario (models.Model) :
    monto_anual = models.IntegerField (max_length = 10, default = 10000)
    extra_junio = models.BooleanField (default = True)
    extra_nobiembre = models.BooleanField (default = True)

class Trabajo (models.Model) :
    titulo = models.CharField (max_length = 50)
    descripsion = models.TextField (max_length = 200)

    salario = models.ManyToManyField (Salario)

class Empleado (models.Model) :
    nombre = models.CharField (max_length = 30)
    apellido = models.CharField (max_length = 30)
    ci = models.CharField (max_length = 30)
    direccion = models.CharField (max_length = 30)
    email = models.EmailField(max_length = 50)

    trabajo = models.ForeignKey (Trabajo, on_delete = models.CASCADE)
    local = models.ForeignKey (Local, on_delete = models.CASCADE)