from django.urls import path
from .import views

#   asi se establese un namespace (espacio de nombres) se usa para identificar el archivo urls de una app espesifica
app_name = 'tareas'

urlpatterns = [
    path ("inicio/", views.inicio, name = "inicio"),
    path ("crear_tarea/", views.crear_tarea, name = "crear_tarea"),

    path ("ver_tareas/", views.ver_tareas, name = "ver_tareas"),
    path ("ver_tareas/<letter>/", views.ver_tareas, name = "ver_tareas"),

    path ("borrar_tarea/<id_tarea>/", views.borrar_tarea, name = "borrar_tarea"),
    path ("editar_tarea/<id_tarea>/", views.editar_tarea, name = "editar_tarea"),
]
