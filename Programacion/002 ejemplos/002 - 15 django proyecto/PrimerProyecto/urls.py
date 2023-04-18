from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ("", views.inisio, name = "inicio" ),
    path ("donde_vivo/", views.donde_vivo, name = "donde_vivo"),
    path ("futuro/", views.futuro, name = "futuro")
]
