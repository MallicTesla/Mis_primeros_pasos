from django.urls import path
from . import views

urlpatterns = [
    path ("", views.inicio, name = "inicio"),
    path ("menu/", views.menu, name = "menu"),
    path ("crear/", views.crear, name = "crear"),
    path ("empleado/", views.empleado, name = "empleado"),
    path ("local/", views.local, name = "local"),
    path ("departamento/", views.departamento, name = "departamento"),
    path ("pais/", views.pais, name = "pais"),
    path ("trabajo/", views.trabajo, name = "trabajo"),
    path ("salario/", views.salario, name = "salario"),
]