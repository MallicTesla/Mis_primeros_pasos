from django.urls import path
from . import views

urlpatterns = [
    path ("crear/", views.crear, name = "crear"),
    path ("contenido/", views.contenido, name = "contenido"),
    path ("", views.inicio, name = "inicio"),
    # path ("inicio/", views.inicio, name = inicio),
    path ("mostrar/", views.mostrar, name = "mostrar"),
]