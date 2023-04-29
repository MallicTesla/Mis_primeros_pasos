from django.urls import path
from. import views

urlpatterns = [
    path ("consulta/", views.consulta, name = "consultas" ),
    path ("actualizacion/", views.actualizacion, name = "actualizacion")
]