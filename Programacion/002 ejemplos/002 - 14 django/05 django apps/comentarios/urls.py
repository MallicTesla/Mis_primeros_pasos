from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path ("test/", views.test, name = "test" ),
    path ("crear/", views.crear, name = "crear"),
    path ("borrar/", views.borrar, name = "borrar")
]