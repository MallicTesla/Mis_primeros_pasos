from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path ('admin/', admin.site.urls),
    path ("mensajes/", include ("mensajes.urls")),
    path ("url_parametro_opsional/", include ("url_parametro_opsional.urls")),
    path ("filtros/", include ("filtros.urls"))
]
