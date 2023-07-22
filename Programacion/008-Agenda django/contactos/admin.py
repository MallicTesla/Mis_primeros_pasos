from django.contrib import admin
from .models import Contacto, Grupo

class ContactoAdmin (admin.ModelAdmin):
    list_display = ("nombre", "apellido",)
    search_fields = ("nombre", "apellido",)
    list_filter = ("nombre","fecha_registro",)
    date_hierarchy = "fecha_registro"

admin.site.register(Contacto,ContactoAdmin)

class GrupoAdmin (admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)

    #   Esto agregará la opción de seleccionar contactos al editar un grupo
    filter_horizontal = ("contactos",)

admin.site.register(Grupo,GrupoAdmin)