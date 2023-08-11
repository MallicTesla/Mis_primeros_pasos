from django.contrib import admin
from django.urls import path
from tareas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ("", views.menu, name = "menu"),
    path ("registro/", views.registro, name = "registro" ),
]
