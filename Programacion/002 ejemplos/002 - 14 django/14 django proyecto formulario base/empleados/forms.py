from django.forms import ModelForm
from django import forms
from .models import Empleado, Local, Departamento, Pais, Trabajo, Salario

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = "__all__"

class LocalForm(ModelForm):
    class Meta:
        model = Local
        fields = "__all__"

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = "__all__"

class PaisForm(ModelForm):
    class Meta:
        model = Pais
        fields = "__all__"

class TrabajoForm(ModelForm):
    class Meta:
        model = Trabajo
        fields = "__all__"

class SalarioForm(ModelForm):
    class Meta:
        model = Salario
        fields = "__all__"


    # mensage = forms.CharField ( label = "Mensage",
    #                             widget = forms.Textarea (attrs = {"class" : "form-control"})
    #                             )
