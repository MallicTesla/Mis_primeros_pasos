#   normalmente para hacer los formularios se crea un archibo para definir las clases de los formularios

from typing import Any, Dict
from django import forms

class Comentario (forms.Form) :
    #   label = "el texto que va antes de la caja de texto no es nesesario colocarle los dos puntos :",help_text="texto al final de la caja de texto"
    nombre = forms.CharField (label = "pone tu nombre", max_length = 100, help_text = "maximo 100 caracteres")
    #   required espesifica si el campo es obligatorio o no     initial="con el texto que inicia por defecto"
    url = forms.URLField (label = "tu sitio Wed", required = False, initial = "http://")
    #   si no se le pasa un label se coloca el nombre de la variavle 
    comentario = forms.CharField ()
    #   el boton para guardarlo se coloca en el html

class ContactoForm (forms.Form) :
    nombre = forms.CharField (  label = "Nombre",
                                #   no deja escrivir mas de 50 caracteres
                                max_length = 50,
                                #   widget = espesifica el tipo de imput y que atrivutos deve de tener con attrs = {se le pasa una clase de css}
                                #   widget = forms.TextInput (attrs = {"class" : "imput"})
                                widget = forms.TextInput (attrs = {"class" : "form-control"})
                                )

    email = forms.EmailField (  label = "Email",
                                max_length = 50,
                                #   EmailInputpide que si o si alla un @ en el campo ingresado y termine con un . segudo de 2 caracteres
                                widget = forms.EmailInput (attrs = {"class" : "form-control"})
                                )

    mensage = forms.CharField ( label = "Mensage",
                                widget = forms.Textarea (attrs = {"class" : "form-control"})
                                )

    #   asi se agregan mas validasiones a un campo se tiene que agregar clean_ antes del campo
    def clean_nombre (self) :
        nombre = self.cleaned_data.get("nombre")
        if nombre != "Mallic" :
            #   coloca este mensaje de error en el campo
            raise forms.ValidationError ("solo se puede colocar Mallic")

        else :
            return nombre