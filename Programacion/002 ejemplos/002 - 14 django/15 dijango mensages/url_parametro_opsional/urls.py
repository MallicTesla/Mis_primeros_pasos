from django.urls import path
from . import views

urlpatterns = [
    #   para pasar una variavle por url y que la variavle sea opcional se tiene que hacer otro path igual pero que inclulla la variavle y
    #   y en la funcion del views se le tiene que agregar un valor por defecto a la variavle
    path ("", views.opcional, name = "opcional"),
    path ("<str:nombre>", views.opcional, name = "opcional"),
]
