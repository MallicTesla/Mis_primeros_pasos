from django.urls import path
from .import views

#   asi se establese un namespace (espacio de nombres) se usa para identificar el archivo urls de una app espesifica
app_name = 'contactos'

urlpatterns = [
    path ("inicio/", views.inicio, name = "inicio"),
    path ("crear_contacto/", views.crear_contacto, name = "crear_contacto"),
    path ("crear_grupo/", views.crear_grupo, name = "crear_grupo"),
    path ("relacionamiento/", views.relacionar_contacto_grupo, name = "relacionar_contacto_grupo"),
    path ("ver_contactos/", views.ver_contacto, name = "ver_contacto"),
    path ("ver_grupos/", views.ver_grupos, name = "ver_grupos"),
    path ("remober_grupo/<int:id_contacto>/<int:id_grupo>/", views.remober_grupo, name = "remober_grupo" ),
    path ("remober_contacto/<int:id_contacto>/<int:id_grupo>/", views.remober_contacto, name = "remober_contacto" ),
]
