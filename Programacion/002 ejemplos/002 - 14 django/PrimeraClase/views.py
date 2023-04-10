#   todas las funsiones deven de resivir un parametro llamado (request)
from django.http import HttpResponse

#   despues de crarar la funcion se define la vista en el fichero urls.py
def saludo (request) :
    #   HttpResponse con el mensaje de texto "Funcionara". Luego, cuando el usuario hace una solicitud a esta vista, el servidor devuelve una respuesta con el mensaje "Funcionara".
    return HttpResponse ("Funcionara")

def despedida (request) :
    return HttpResponse ("Menos mal que funciono")