from .models import Proyecto
from rest_framework import viewsets, permissions
from .sarializers import ProyectoSerializers

#   aca se definen las consultas que se pueden hacer
class ProyectoViewSet (viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    #   aca asignas los permisos para quien puede realisar las consultas
    #   AllowAny        cualquiera puede solisitar
    #   IsAuthenticated comprueva si esta aunteticado
    permission_classes = [permissions.AllowAny]
    serializer_class = ProyectoSerializers
