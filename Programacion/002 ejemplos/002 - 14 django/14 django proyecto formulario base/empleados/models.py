from django.db import models

class Empleado (models.Model) :
    nombre = models.CharField (max_length = 30)
    apellido = models.CharField (max_length = 30)
    ci = models.CharField (max_length = 30)
    direccion = models.CharField (max_length = 100)
    email = models.EmailField(max_length = 50)

    def __str__(self) :
        return f"{self.nombre} {self.apellido}"

class Local (models.Model) :
    local_nombre = models.CharField (max_length = 50)
    direccion = models.CharField (max_length = 50)

    empleado = models.ForeignKey (Empleado, on_delete = models.SET_NULL, null=True)

    def __str__(self) :
        return self.local_nombre

class Departamento (models.Model) :
    departamento = models.CharField (max_length = 30)

    local = models.ForeignKey (Local, on_delete = models.SET_NULL, null=True)

    def __str__(self) :
        return self.departamento

class Pais (models.Model) :
    nombre = models.CharField (max_length = 30)

    departamento = models.ForeignKey (Departamento, on_delete = models.SET_NULL, null=True)

    def __str__(self) :
        return self.nombre

class Trabajo (models.Model) :
    titulo = models.CharField (max_length = 50)
    descripsion = models.TextField ()

    empleado = models.ForeignKey (Empleado, on_delete = models.SET_NULL, null=True)

    def __str__(self) :
        return self.titulo

class Salario (models.Model) :  
    monto_anual = models.IntegerField (default = 10000)
    extra_junio = models.BooleanField (default = True)
    extra_nobiembre = models.BooleanField (default = True)

    trabajo = models.ForeignKey (Trabajo, on_delete = models.SET_NULL, null=True)

    def __str__(self) :
        return self.monto_anual
