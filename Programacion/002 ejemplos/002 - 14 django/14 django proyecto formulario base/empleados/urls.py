from django.urls import path, re_path
from . import views

urlpatterns = [
    path ("", views.inicio, name="inicio"),

    path ("menu_crear/", views.menu_crear, name="menu_crear"),
    path ("menu_ver/", views.menu_ver, name="menu_ver"),

    path ("<resource>/empleado/", views.empleado, name="empleado"),
    path ("<resource>/local/", views.local, name="local"),
    path ("<resource>/departamento/", views.departamento, name="departamento"),
    path ("<resource>/pais/", views.pais, name="pais"),
    path ("<resource>/trabajo/", views.trabajo, name="trabajo"),
    path ("<resource>/salario/", views.salario, name="salario"),

    re_path (r'^(?P<resource>.+)/editar/(?P<id>\d+)/$', views.editar, name = "editar"),
    re_path (r'^(?P<resource>.+)/borrar/(?P<id>\d+)/$', views.borrar, name = "borrar"),
    re_path (r'^(?P<resource>.+)/relaciones/(?P<id>\d+)/$', views.relaciones, name = "relaciones"),
]

