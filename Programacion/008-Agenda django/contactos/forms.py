from django import forms
from django.forms import ModelForm
from .models import Contacto, Grupo

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__"
        exclude = ("fecha_registro",)

    # asi le agrego un estilo css al formulario si ya tengo el modelo echo
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields ['nombre'].widget.attrs.update ({'class': 'campo-form'})
        self.fields ['apellido'].widget.attrs.update ({'class': 'campo-form'})
        self.fields ['cel'].widget.attrs.update ({'class': 'campo-form'})
        self.fields ['tel'].widget.attrs.update ({'class': 'campo-form'})
        self.fields ['email'].widget.attrs.update ({'class': 'campo-form'})
        self.fields ['trabajo'].widget.attrs.update ({'class': 'campo-form'})
        self.fields ['nota'].widget.attrs.update ({'class': 'campo-form'})

class GrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = "__all__"
        exclude = ("contactos",)

    def __init__ (self, *args, **kwargs):
        super().__init__ (*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'campo-form'})

# esta clase es para trabajar con la tercer trabla de relacionamientos de los modelos
# esta clase es para crear un formulario con menus deplegables para relacinar
class Relacionar_Contacto_GrupoForm (forms.Form):
    #   ModelChoiceField es para crear un menu desplegable
    #   queryset rellena el menu desplegable con los rts del modelo
    contacto = forms.ModelChoiceField(  queryset = Contacto.objects.all(),
                                        widget=forms.Select (attrs={'class': 'campo-form'}))
    #   asi se agrega el estilo en este caso
    grupo = forms.ModelChoiceField(     queryset = Grupo.objects.all(),
                                        widget=forms.Select (attrs={'class': 'campo-form'}))

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