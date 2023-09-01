#   documentacion https://www.django-rest-framework.org/

from rest_framework import serializers
from .models import Proyecto

#   asi se combierte un modelo en datos para ser consultados a traves de jason
class ProyectoSerializers (serializers.ModelSerializer):
    #   se rellena como si fuera un formulario
    class Meta :
        model = Proyecto
        fields = "__all__"
        #   asi espesificas que campo queres que sea solo de lectura
        read_only_fields = ("agregado", )

