#   normalmente para hacer los formularios se crea un archibo para definir las clases de los formularios

from django import forms

class Comentario (forms.Form) :
    #   label = "el texto que va antes de la caja de texto no es nesesario colocarle los dos puntos :",help_text="texto al final de la caja de texto"
    nambre = forms.CharField (label = "pone tu nombre", max_length = 100, help_text = "maximo 100 caracteres")
    #   required espesifica si el campo es obligatorio o no     initial="con el texto que inicia por defecto"
    url = forms.URLField (label = "tu sitio Wed", required = False, initial = "http://")
    #   si no se le pasa un label se coloca el nombre de la variavle 
    comentario = forms.CharField ()
    #   el boton para guardarlo se coloca en el html