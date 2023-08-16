from django.contrib import admin
from .models import Tarea

class TareaAdmoin (admin.ModelAdmin) :
    #   todos los campos que son agregados son de solo lectura
    #   se le pasa una tupla con los campos deseados
    readonly_fields = ("creado",)

#   asi mostras la tabla de forma simple
admin.site.register(Tarea, TareaAdmoin)

