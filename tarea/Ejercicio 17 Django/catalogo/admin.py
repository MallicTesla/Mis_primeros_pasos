from django.contrib import admin
from .models import Director, Genero, Pelicula, Instancia_pelicula

admin.site.register(Director)
admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(Instancia_pelicula)