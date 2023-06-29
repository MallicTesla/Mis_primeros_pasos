from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ("", views.menu_inicio, name = "menu_inicio"),
    path ("contactos/", include ("contactos.urls")),
    path ("tareas/", include ("tareas.urls")),
]
