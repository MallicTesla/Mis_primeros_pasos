# from django import views
from catalog import views
from django.urls import path

#   la letra (r)es una expresion regular esto quiere desir que cuando la petision sea / nada ("^$" quiere desir que empiesa y termina con nada) 
#   se ejecuta lo siguiente en este caso dispara la funcion index del modulo views y la nombra index (name = "index")

urlpatterns = [
    path (r"", views.index , name = "index")
]