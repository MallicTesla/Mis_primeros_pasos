from tkinter import *                       #   https://docs.python.org/es/3/library/tkinter.html
from tkinter import ttk

ventana = Tk ()
ventana.title("Primera Ventana")            #   Cambiar el nombre de la ventana
ventana.geometry("520x520")                 #   Configurar tamaño
ventana.resizable(1,1)                      #   para modificar manual mente el tamaño (para no modificarla(0,0)) (para modificarlo(1,1))
ventana.config(bg="#500090")                #   Cambiar color de fond el color en inglés o en formato hexadecima

etiqueta = ttk.Frame(ventana, padding=100,)  #   crea una etiqueta para el widget que contiene una cadena de texto (tamaño del eidget).
etiqueta.grid(padx= 35, pady=46 )          #   grid especificar la posición de la etiqueta que está dentro del marco del widget

ttk.Label(etiqueta, text="funcionara").grid(column=0, row=0)    #   crea una etiqueta para el widget que contiene una cadena de texto estática (donde esta, texto).grid especificar la posición de
ttk.Button(etiqueta, text="Quitar", command=ventana.destroy).grid(column=1, row=0) #   crra un boton (donde esta, texto del boton, funcion del boton,)


etiqueta_01= ttk.Frame(ventana, padding=10,)
etiqueta_01.grid(padx= 250, pady=260) 
ttk.Button(etiqueta_01, text="Quita", command=ventana.destroy).grid(column=1, row=0) 
ttk.Label(etiqueta_01, text="funcionar").grid(column=0, row=0)





ventana.mainloop()