from django.contrib import admin

# aca se registran los modelos para administrarlos desde el panel de administracion en el nabegador 

from .models import Producto

class ProductoAdmin (admin.ModelAdmin):
    #   aca colocas los campos que queres que se vean en el panel de administracion por defecto se coloca el str del modelo
    list_display = ("nombre","vreve_descripcion","stock",)
    #   asi se agrega un buscador y se le dise que campos tiene que buscar
    search_fields = ("nombre","vreve_descripcion",)
    #   asi se agrega un buscador por filtros se agrega el campo por el cual deseas filtrar (podria ser el campo categoria o tipo)
    #   si se agrega un filtro de fechas te agrega un filtro por rango de fecha
    list_filter = ("nombre","descuento_asta",)
    #   asi se agrega un filtro por gerarquia en este caso que se usa un campo de fechas aparese el filtro por meses
    date_hierarchy = "descuento_asta"

admin.site.register(Producto,ProductoAdmin)
#   en el administrador de django se puede vuer el nombre del modelo pero en plural y si esta separado por un gion _ este se separa solo
#   ademas si en el campo del modelo colocas este atributo (verbose_name="Nombre del producto") se rellena con ese valor
#   se muestrn solo los valores definidos en el str del modelo si no se coloca el str se muestra la palabra objet indicando que existe un objeto
