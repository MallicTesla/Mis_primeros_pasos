from django.forms import ModelForm
from .models import Producto, Todo

#   y asi se hace un filtro por formulario
class ProductoForm(ModelForm):
    class Meta :
        modol = Producto
        fiels = "__all__"
        # widgets = {
        #     "nombre": TextInput (attrs = {"type": "text"}),
        # }