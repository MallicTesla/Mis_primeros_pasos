from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),

    path("menu_crear/", views.menu_crear, name="menu_crear"),
    path("menu_ver/", views.menu_ver, name="menu_ver"),

    path("<str:resource>/empleado/", views.empleado, name="empleado"),
    path("<str:resource>/local/", views.local, name="local"),
    path("<str:resource>/departamento/", views.departamento, name="departamento"),
    path("<str:resource>/pais/", views.pais, name="pais"),
    path("<str:resource>/trabajo/", views.trabajo, name="trabajo"),
    path("<str:resource>/salario/", views.salario, name="salario"),
]

#   <str:resource> aca se coloca la url que le pasas en el link del html