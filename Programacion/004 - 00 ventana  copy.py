from tkinter import *
from tkinter import ttk

ventana = Tk ()
ventana.title("Primera Ventana")        #   Cambiar el nombre de la ventana
ventana.geometry("520x520")             #   Configurar tamaño
ventana.resizable(1,1)                  #   para modificar manual mente el tamaño (para no modificarla(0,0)) (para modificarlo(1,1))
ventana.config(bg="#500090")            #   Cambiar color de fond el color en inglés o en formato hexadecima
etiqueta = ttk.Frame(ventana, padding=10,)   #   crea una etiqueta para el widget que contiene una cadena de texto (tamaño del eidget).
etiqueta.grid(padx= 350, pady=460)           #   grid especificar la posición de la etiqueta que está dentro del marco del widget
ttk.Button(etiqueta, text="Quitar", command=ventana.destroy).grid(column=1, row=0)  #   crra un boton (posision, texto del boton, funcion del boton,)
ttk.Label(etiqueta, text="funcionara").grid(column=0, row=0)







ventana.mainloop()