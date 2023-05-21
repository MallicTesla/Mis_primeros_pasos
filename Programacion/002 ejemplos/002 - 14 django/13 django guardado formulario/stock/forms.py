from django.forms import ModelForm
from .models import Producto

class ProductoForm (ModelForm) :
    class Meta :
        model = Producto
        fields = "__all__"
