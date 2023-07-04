from django import forms
from django.forms import ModelForm
from .models import Tarea

class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = "__all__"
        exclude = ("fecha_registro",)