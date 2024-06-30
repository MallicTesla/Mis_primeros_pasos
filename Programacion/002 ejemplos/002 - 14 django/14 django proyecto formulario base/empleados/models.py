from django.db import models

class Salario (models.Model):
    monto_anual = models.IntegerField(default=10000)
    extra_junio = models.BooleanField(default=True)
    extra_noviembre = models.BooleanField(default=True)

    def __str__(self):
        return str(self.monto_anual)

class Trabajo(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()

    salario = models.ForeignKey(Salario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

class Pais(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    departamento = models.CharField(max_length=30)

    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.departamento

class Local(models.Model):
    local_nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.local_nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    ci = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

    trabajo = models.ForeignKey(Trabajo, on_delete=models.SET_NULL, null=True)
    local = models.ForeignKey(Local, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
