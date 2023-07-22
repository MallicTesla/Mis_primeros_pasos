from django.contrib import admin
from .models import Tarea

class TareaAdmin (admin.ModelAdmin):
    list_display = ("titulo", "breve_descripcion",)
    search_fields = ("titulo", "breve_descripcion",)
    list_filter = ("titulo","fecha_registro",)
    date_hierarchy = "fecha_registro"

admin.site.register(Tarea,TareaAdmin)