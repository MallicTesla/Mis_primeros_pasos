import tkinter                       #   hhttps://recursospython.com/guias-y-manuales/caja-de-texto-entry-tkinter/
from tkinter import ttk

ventana = tkinter.Tk()

ventana.title("Descargas You Tuve")         #   Cambiar el nombre de la ventana
ventana.geometry("700x700")                 #   Configurar tamaño
ventana.resizable(1,1)                      #   para modificar manual mente el tamaño (para no modificarla(0,0)) (para modificarlo(1,1))
ventana.config(bg="#500090")                #   Cambiar color de fond el color en inglés o en formato hexadecima


ventana.columnconfigure (0, weight = 1)


# link------------------------------------------------------------------------------------------
saludo = tkinter.Label(ventana,     text = "Link de Descarga",
                                    bg = "#500090",
                                    fg = "red",
                                    font="arial 15 ",)
saludo.grid(column = 0, row = 1, pady = 5, padx = 5)

# texto.
entry = tkinter.Entry(ventana,      width = "75",
                                    font="arial 15 ",)
# Posicionarla en la ventana.
entry.grid(column = 0, row = 2, pady = 5, padx = 5, columnspan=3)


# radio boton -----------------------------------------------------------------------------------
freim = tkinter.Frame (ventana, bg = "blue",)
freim.grid (column = 0, row = 3, ipady= 40)

selecsion = tkinter.StringVar()

r1 = tkinter.Radiobutton(freim,     text = "MP 3",
                                    value = "1",                #   el valor que entrega cuando es selecsionado 
                                    bg = "red",
                                    fg = "blue",
                                    font = "arial 15",
                                    variable = selecsion)      #   variable = el nombre de la variavle del valor selecsionado
r1.pack(side="left", padx=5)

r2 = tkinter.Radiobutton(freim,     text = "Video",
                                    value = "2",                #   el valor que entrega cuando es selecsionado 
                                    bg = "red",
                                    fg = "blue",
                                    font = "arial 15",
                                    variable = selecsion)      #   variable = el nombre de la variavle del valor selecsionado
r2.pack(side="left", padx=5)

r3 = tkinter.Radiobutton(freim,     text = "Descarga rapida",
                                    value = "3",                #   el valor que entrega cuando es selecsionado 
                                    bg = "red",
                                    fg = "blue",
                                    font = "arial 15",
                                    variable = selecsion)      #   variable = el nombre de la variavle del valor selecsionado
r3.pack(side="left", padx=5)


# calidad --------------------------------------------------------------------------------------------------------------------------
freim_1 = tkinter.Frame (ventana, bg = "blue",)
freim_1.grid (column = 0, row = 4, ipady= 20)

calidad_t = tkinter.Label (freim_1, text = "Resolucion",
                                    bg = "red",
                                    fg = "blue",
                                    font="arial 15 ",)
calidad_t.pack(side="left", padx=5)

calidad_i = tkinter.Entry(freim_1,  width = "5",
                                    font="arial 15 ",)
calidad_i.pack(side="left", padx=5)

calidad_t = tkinter.Label (freim_1, text = "p",
                                    bg = "red",
                                    fg = "blue",
                                    font="arial 15 ",)
calidad_t.pack(side="left", padx=5)


# boton provar --------------------------------------------------------------------------------------------------------------------------
boton_1 = tkinter.Button(ventana,   text = "Resolusiones disponibles",
                                    width = "50",
                                    bg = "red",
                                    fg = "blue",
                                    font = "arial 15",)
boton_1.grid (column = 0, row = 5)

# Texto de salida ------------------------------------------------------------------------------------------------------------------
freim_2 = tkinter.Frame (ventana,   bg = "blue")
freim_2.grid (column = 0, row = 6, ipadx = 0, ipady= 0)


txt_salida = tkinter.Label (freim_2,    text = "texto",
                                        font = "arial 15",
                                        width= 50,
                                        height = 13,
                                        # justify="left",
                                        anchor="nw"
                                        )
txt_salida.pack(side="top", padx=5)

# informacion = tkinter.StringVar()
# informacion.set ("Texto de salida")

# txt_salida = tkinter.Text (freim_2, font = "arial 15",
#                                     height = "10",
#                                     width = "51",
#                                     wrap = "word",
#                                     state="disabled",)
# txt_salida.pack(fill="both", pady= 20)

# txt_salida.insert("1.0", "Texto de salida")
# scrollbar = tkinter.Scrollbar(freim_2, command=txt_salida.yview)
# scrollbar.pack(side="right", fill="y")
# txt_salida.config(yscrollcommand=scrollbar.set)

# Boton descarga ---------------------------------------------------------------------------------------------------------
boton_1 = tkinter.Button(ventana,   text = "Descargar",
                                    width = "50",
                                    bg = "red",
                                    fg = "blue",
                                    font = "arial 15",)
boton_1.grid (column = 0, row = 7)





ventana.mainloop()

# etiqueta = ttk.Frame(ventana, padding=10,)  #   crea una etiqueta para el widget que contiene una cadena de texto (tamaño del eidget).
# etiqueta.grid(padx= 350, pady=400 )          #   grid especificar la posición de la etiqueta que está dentro del marco del widget

# ttk.Label(etiqueta, text="funcionara").grid(column=0, row=0)    #   crea una etiqueta para el widget que contiene una cadena de texto estática (donde esta, texto).grid especificar la posición de
# ttk.Button(etiqueta, text="Quitar", command=ventana.destroy).grid(column=2, row=0) #   crra un boton (donde esta, texto del boton, funcion del boton,)



# entry = ttk.Entry(state=tk.DISABLED)              #para que aparesca el input en gris
# entry.config(state=tk.NORMAL)                     #asi lo sacas de gris

