from django.urls import path
from . import views

urlpatterns = [
    path ("", views.filtro, name = ""),

]
