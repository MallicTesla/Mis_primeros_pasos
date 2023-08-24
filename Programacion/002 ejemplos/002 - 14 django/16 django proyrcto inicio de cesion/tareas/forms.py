from django.forms import ModelForm
from django import forms
from .models import Tarea

class TareaForm (ModelForm):
    class Meta:
        model = Tarea
        fields = ["titulo", "descripsion", "importansia"]
        widgets = {
            "titulo": forms.TextInput (attrs = {"class":"form-control", "placeholder":"Titulo descriptivo"}),
            "descripsion": forms.Textarea (attrs = {"class":"form-control", "placeholder":"Pone la descripsion"}),
            "importansia": forms.CheckboxInput (attrs = {"class":"form-check-input"}),
        }