"""PrimeraClase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# se importa la funcion
from . import views

#   se crea una nueva ruta con la funcion creada en views
urlpatterns = [
    path('admin/', admin.site.urls),
    # primero se crea el nombre de la ruta y despues va la funcion u despues se puede colocar un nombre a esta ruta para usarla mas adelante para no andar escriviendo toda la ruta
    path ("saludo/", views.saludo, name = "saludo"),
    path ("despedida/", views.despedida, name = "despedida")
]
