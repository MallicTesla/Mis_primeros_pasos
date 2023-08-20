from django.contrib import admin
from django.urls import path
from tareas import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path ("", views.menu, name = "menu"),

    path ("registro/", views.registro, name = "registro"),
    path ("iniciar_sesion/", views.iniciar_sesion, name = "iniciar_sesion"),
    path ("salir/", views.salir, name = "salir"),

    path ("crear_tarea/", views.crear_tarea, name = "crear_tarea"),
    path ("tareas/", views.tareas, name = "tareas"),
    path ("tarea/<int:tarea_id>", views.tarea, name = "tarea"),
    path ("tarea/<int:tarea_id>/completa", views.tarea_completa, name = "tarea_completa"),
    path ("tarea/<int:tarea_id>/borada", views.borar_tarea, name = "borar_tarea")
]
