from django import views
from django.conf.urls import url

#   la letra (r)es una expresion regular esto quiere desir que cuando la petision sea / nada ("^$" quiere desir que empiesa y termina con nada) 
#   se ejecuta lo siguiente en este caso dispara la funcion index del modulo views y la nombra index (name = "index")

urlpatterns = [
    url (r"^$", views.index, name = "index")
]