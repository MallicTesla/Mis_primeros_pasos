from django.urls import path
from .import views

#   asi se establese un namespace (espacio de nombres) se usa para identificar el archivo urls de una app espesifica
app_name = 'tareas'

urlpatterns = [
    path ("inicio/", views.inicio, name = "inicio"),
    path ("crear_tarea/", views.crear_tarea, name = "crear_tarea"),
]
