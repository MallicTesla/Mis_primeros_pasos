from django import forms
from django.forms import ModelForm
from .models import Contacto, Grupo

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__"
        exclude = ("fecha_registro",)

class GrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = "__all__"
        exclude = ("contactos",)

# esta clase es para trabajar con la tercer trabla de relacionamientos de los modelos
# esta clase es para crear un formulario con menus deplegables para relacinar
class Relacionar_Contacto_GrupoForm(forms.Form):
    #   ModelChoiceField es para crear un menu desplegable
    #   queryset rellena el menu desplegable con los rts del modelo
    contacto = forms.ModelChoiceField(queryset = Contacto.objects.all())
    grupo = forms.ModelChoiceField(queryset = Grupo.objects.all())

class EliminarRelacionForm(forms.Form):
    # grupo = forms.ModelChoiceField(queryset=Grupo.objects.all())
    # contacto = forms.ModelChoiceField(queryset=Contacto.objects.none())

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if 'grupo' in self.data:
    #         grupo_id = self.data.get('grupo')
    #         self.fields['contacto'].queryset = Contacto.objects.filter(grupo__id=grupo_id)
    #     else:
    #         self.fields['contacto'].queryset = Contacto.objects.none()
    ...