from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ("", views.inisio, name = "inicio" ),
    path ("perfil/", views.perfil, name = "perfil"),
    path ("trabajos/", views.trabajos, name = "trabajos")
]
