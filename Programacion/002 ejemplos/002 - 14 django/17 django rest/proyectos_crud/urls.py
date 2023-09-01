#   rest crea las rutas vasicas automaticamente asi
from rest_framework import routers
from .api import ProyectoViewSet
#   se tiene que ejecutar el modelo routers
router = routers.DefaultRouter()

#   se da un nombre a la ruta y seguido de donde toma los datos 
router.register ("api/proyecto", ProyectoViewSet, "proyectos")

urlpatterns = router.urls
