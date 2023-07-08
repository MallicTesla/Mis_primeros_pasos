from django import forms
from django.forms import ModelForm
from .models import Tarea

class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = "__all__"
        exclude = ("fecha_registro",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields ['titulo'].widget.attrs.update ({'class': 'campo-form'})
        self.fields ['breve_descripcion'].widget.attrs.update ({'class': 'campo-form'})
        self.fields ['descripcion'].widget.attrs.update ({'class': 'campo-form'})