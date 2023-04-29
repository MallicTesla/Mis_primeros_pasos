from django.shortcuts import render
from .models import Autor,Entrada

def consulta (riquest) :
    #   para optener todos los elementos de Autor
    autores = Autor.objects.all ()

    #   para optener todas las coinsidensias
    filtro = Autor.objects.filter (email = "acostalarry@example.net")

    #   para optener un unico objeto
    autor = Autor.objects.get (id = 35)

    #   asi se optiene una cantidad limitada (con [:10] se optienen los 10 primeros)
    limitado = Autor.objects.all () [:10]

    #   asi se optiene una cantidad limitada (con [5:10] se salta 5 renglones y luego devuelve los valores asta el renglon 10)
    salteados = Autor.objects.all () [5:10]

    #   ordena todos por el email
    ordenados = Autor.objects.all ().order_by ("email")

    #   al campo en el que queremos hacerle la busqueda se agrega 2 baras baja __ y luego se agregan las inisiales en ingles del operador

    #       __lte       menor o igual   (lower than equals)
    #       __get       mayor o igual   (greter than equals)
    #       __lt        menor que       (lower than)
    #       __gt        mayor que       (greater than)
    #       __contains  contirne
    #       __exact     exacto

    #   entrega todo los balores por devajo o igual a 15
    rango_id = Autor.objects.filter(id__lte=15)

    #   entrega todos los nombres que tengan "food"
    filtro_nombre = Autor.objects.filter (nombre__contains = "food")


    #   la variavle con el objeto va dentro de {"nombre a darle que se va a usar en el HTML": variavle} y asi le pasas esa informasion al html
    return render (riquest, "post/consulta.html", { "autores": autores, 
                                                    "filtro": filtro, 
                                                    "autor": autor, 
                                                    "limitado": limitado, 
                                                    "salteados": salteados,
                                                    "ordenados": ordenados,
                                                    "rango_id": rango_id,
                                                    "filtro_nombre": filtro_nombre, })
