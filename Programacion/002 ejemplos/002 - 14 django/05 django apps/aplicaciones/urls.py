from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #   para incluir urls de las apps se llama al modulo include 
    #   primero se coloca el nombre de la ruta y despues se coloca el nombre se la app punto el archivo donde estan las rutas
    path ("comentarios/", include ("comentarios.urls"))
]
