from django.forms import ModelForm
#   se llaman los modelos nesesarios
from .models import Empleado

#   para crear un formulario con los modelos se crea una clase con el mismo nombre del modelo seguido de Form
class EmpladosForm (ModelForm) :
    #   despues se crea una clase Meta y se asosia el modelo deseado
    class Meta :
        model = Empleado
        #   ay que espesificar los campos que queres mostrar en el html
        # fields = ["nombre", "apellido", "email"]

        #   asi se agregan todos los campos de l modelo
        fields = "__all__"

        #   asi se inclullen todo los campos menos el selcsionado
        # exclude = ("email",)

        #   asi se agregan campos que no estan en el modelo
        # extra_fields = ["salario",]