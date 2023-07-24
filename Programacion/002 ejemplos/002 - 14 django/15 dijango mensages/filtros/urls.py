from django.urls import path
from . import views

urlpatterns = [
    path ("<letra>", views.filtro, name = "filtro"),

]
