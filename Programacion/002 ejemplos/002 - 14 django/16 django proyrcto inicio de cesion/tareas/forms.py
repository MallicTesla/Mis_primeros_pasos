from django.forms import ModelForm
from .models import Tarea

class TareaForm (ModelForm):
    class Meta:
        model = Tarea
        fields = ["titulo", "descripsion", "importansia"]