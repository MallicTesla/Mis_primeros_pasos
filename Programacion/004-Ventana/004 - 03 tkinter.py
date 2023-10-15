import tkinter
from tkinter import ttk
import random
ventana = tkinter.Tk()

ventana.title("Primera Ventana")    
ventana.geometry("500x500")
ventana.resizable(1,1)
ventana.config(bg="#500090") 

#--------------------------------------------------------------pack--------------------------------------------------------------

# saludo = tkinter.Label(ventana, text = "Hola",
#                                 bg = "red",
#                                 fg = "blue",
#                                 font="arial 15 ",)
# # saludo.pack(ipadx = 50, ipady = 50 , fill = "x")      #   con fille = x se ajusta el wiget al ancho de la ventana cuando lo modificas y con fille = both lo hace en ambas direcsiones
# # saludo.pack(ipadx = 50, ipady = 50 , expand = True)   #   mantiena el wigt centrado con sus medidas cuando modifica el tamaño 
# saludo.pack(ipadx = 50, ipady = 50 , side = "left")     #   se posiciona el wiget centrado  a la Izquierda

# adios = tkinter.Label(ventana, text = "Adios",
#                                 bg = "green",
#                                 fg = "blue",
#                                 font="arial 15 ",)
# adios.pack(fill = "both", expand = True)               #    con fille = y se ajusta el wiget al alto de la ventana cuando lo modificas fille = both lo hace en ambas direcsiones

# -------------------------------------------------columnas y filas---------------------------------------------------------------------------------

# ventana.columnconfigure (0, weight = 1)
# ventana.columnconfigure (1, weight = 3)

# usuario_tex = ttk.Label(ventana,    text = "Nombre de Usuario:")
# usuario_tex.grid(column = 0, row = 0, sticky = tkinter.W, padx = 5, pady = 5)  
# #   grid ((columna),(fila),(sticky = tkinter.W(para que se mantenga en el lugar, va por puntos cardinales))(padx y pady son los marjenes que queda alrededor del texto))

# usuario_entrada = ttk.Entry(ventana)
# usuario_entrada.grid(column = 1, row = 0, sticky = tkinter.E, padx = 5, pady = 5)

# contraseña_tex = ttk.Label(ventana,    text = "contraseña:")
# contraseña_tex.grid(column = 0, row = 1, sticky = tkinter.W, padx = 5, pady = 5)

# contraseña_entrada = ttk.Entry(ventana, show = "*")                                     #   show cambia los caracteres visivles de la caja de texto
# contraseña_entrada.grid(column = 1, row = 1, sticky = tkinter.E, padx = 5, pady = 5)

# boton_dale = ttk.Button(ventana, text = "Dale")
# boton_dale.grid(column = 1, row = 3, sticky = tkinter.E, padx = 5, pady = 5)


#-------------------------------------------------------------------por pixeles---------------------------------------------------------------------------------------

# cartel_1 = tkinter.Label(ventana,   text = "acomodado por pixeles",
#                                     bg = "green",
#                                     fg = "blue",
#                                     font="arial 15 ",)
# cartel_1.place(x = 10, y = 50)

# cartel_2 = tkinter.Label(ventana,   text = "otro igual",
#                                     bg = "blue",
#                                     fg = "green",
#                                     font="arial 15 ",)
# cartel_2.place(relx = 0.10, rely = 0.3, relwidth = 0.2 , anchor = "ne")
# #   relx y rely son cordenadas de relativas van segun el porsentaje de la pantalla, relwidth = 0.5: indica el ancho relativo del widget en la ventana ,anchor = "ne": indica el punto de anclaje del widget con puntos cardinales

#-------------------------------------------------------------------------carteles random---------------------------------------------------------------------------------------------

# nombres = ["Pablo","German","franco","Marcelo","Jorge"]
# comidas = ["Pizza", "Hamburguesa", "Sushi", "Ensalada César", "Tacos", "Espaguetis a la boloñesa", "Risotto", "Pene", "Heladdo", "Curry de pollo", "Chorizo", "Pollo al horno", "Pija", "Cheesecake", "Brownie", "Mousse de chocolate", "Flan", "Tiramisú", "Crème brûlée", "Galletas de chispas de chocolate"]
# colores = ["blue","red","black","yellow","green","purple"]

# for x in range (0,5):
#     nombre = random.randint (0, len (nombres)-1)
#     comida = random.randint (0, len (comidas)-1)
#     color_1 = random.randint (0, len (colores)-1)
#     color_2 = random.randint (0, len (colores)-1)
#     cartel = tkinter.Message (ventana,    text = f"{nombres[nombre]} come {comidas[comida]}",
#                                         bg = colores[color_1],
#                                         fg = colores[color_2],
#                                         font="arial 15")
#     cartel.place(x = random.randint (0,350), y = random.randint (0,450))

#---------------------------------------------------------------wigets-------------------------------------------------------------------------
# ---------------------------------------------freim-------------------------------------------------------------------------
#   se pueden colocar cosas adentro

# ventana.columnconfigure (0, weight = 1)
# ventana.columnconfigure (1, weight = 3)

# freim = tkinter.Frame (ventana, bg = "red",)
# freim.grid (column = 0, row = 0, sticky = tkinter.W)

# cartel = tkinter.Label (freim,  text = "hola",
#                                 bg = "blue",
#                                 fg = "green",
#                                 font="arial 15 ",)
# cartel.grid (column = 0, row = 0, sticky = tkinter.W, padx = 50, pady = 50)

#-------------------------------------------list box---------------------------------------------------------------------------------------------

# ventana.columnconfigure (0, weight = 1)
# ventana.columnconfigure (1, weight = 3)

# nombres = ["Pablo","German","franco","Marcelo","Jorge"]
# #   a la lista ahi que transformarla a un formato que soporte tkinter
# lista_items = tkinter.StringVar(value = nombres)

# lista = tkinter.Listbox (ventana,   height = 4,                     #   renglones y tiene Scrol
#                                     bg = "red",
#                                     fg = "blue",
#                                     font="arial 15",
#                                     listvariable = lista_items)     #   listvariable = la lista que quiero mostrar
# lista.grid (column = 0, row = 0, sticky = tkinter.W)

#------------------------------------------------radio boton-------------------------------------------------------------------------------
#   si tienen la misma variavle (variable = selecsion) solo se puede tener activado un boton a la ves

# ventana.columnconfigure (0, weight = 1)
# ventana.columnconfigure (1, weight = 3)

# selecsion = tkinter.StringVar()

# r1 = tkinter.Radiobutton(ventana,   text = "R1",
#                                     bg = "red",
#                                     fg = "blue",
#                                     font = "arial 15",
#                                     value = "1",                #   el valor que entrega cuando es selecsionado 
#                                     variable = selecsion)      #   variable = el nombre de la variavle del valor selecsionado
# r1.grid (column = 0, row = 1, pady = 5, padx = 5)

# r2 = tkinter.Radiobutton(ventana,   text = "R2",
#                                     bg = "red",
#                                     fg = "blue",
#                                     font = "arial 15",
#                                     value = "2",
#                                     variable = selecsion)
# r2.grid (column = 0, row = 2, pady = 5, padx = 5)

# r3 = tkinter.Radiobutton(ventana,   text = "R3",
#                                     bg = "red",
#                                     fg = "blue",
#                                     font = "arial 15",
#                                     value = "3",
#                                     variable = selecsion)
# r3.grid (column = 0, row = 3, pady = 5, padx = 5)

# selecsion2 = tkinter.StringVar()

# r1 = tkinter.Radiobutton(ventana,   text = "Ro1",
#                                     bg = "red",
#                                     fg = "blue",
#                                     font = "arial 15",
#                                     value = "1",
#                                     variable = selecsion2 ,)      #   si hace referensia a otra variavle se puede selecsionar otro boton
# r1.grid (column = 1, row = 1, pady = 5, padx = 5)

# r2 = tkinter.Radiobutton(ventana,   text = "Ro2",
#                                     bg = "red",
#                                     fg = "blue",
#                                     font = "arial 15",
#                                     value = "2",
#                                     variable = selecsion2 ,)
# r2.grid (column = 1, row = 2, pady = 5, padx = 5)

# r3 = tkinter.Radiobutton(ventana,   text = "Ro3",
#                                     bg = "red",
#                                     fg = "blue",
#                                     font = "arial 15",
#                                     value = "3",
#                                     variable = selecsion2 ,)
# r3.grid (column = 1, row = 3, pady = 5, padx = 5)

# ----------------------------------------------check boton--------------------------------------------------------------------------------

# ventana.columnconfigure (0, weight = 1)
# ventana.columnconfigure (1, weight = 3)

# selecsion1 = tkinter.StringVar ()
# selecsion2 = tkinter.StringVar ()

# def funcion () :
#     print ("funciono")
# check1 = tkinter.Checkbutton (ventana,  text = "check1",
#                                         bg = "red",
#                                         fg = "blue",
#                                         font = "arial 15",
#                                         command = funcion,
#                                         variable = selecsion1)
# check1.grid (column = 0, row = 0) 

# check2 = tkinter.Checkbutton (ventana,  text = "check2",
#                                         bg = "red",
#                                         fg = "blue",
#                                         font = "arial 15",
#                                         command = funcion,
#                                         variable = selecsion2)
# check2.grid (column = 1, row = 0)

#-----------------------------------------------botones y eventos------------------------------------------------------------------------

# ventana.columnconfigure (0, weight = 1)
# ventana.columnconfigure (1, weight = 3)

# #   por defecto el boton entrega una variavle (event) que si o si se le deve pasar a la funcion por mas que no la use

# def un_click(event):
#     print(f"hiciste un clic en la posición{event.x},{event.y}")

# # def un_click (event) :
# #     print ("hicistes un clic")

# def doble_click (event) :
#     print (f"hicistes doble clic en la posision {event.x},{event.y}")

# def salir () :
#     ventana.quit()

# boton_1 = tkinter.Button(ventana,   text = "boton_1",
#                                     bg = "red",
#                                     fg = "blue",
#                                     font = "arial 15",)
# boton_1.grid (column = 0, row = 0)



# boton_2 = tkinter.Button(ventana,   text = "Salir",
#                                     bg = "red",
#                                     fg = "blue",
#                                     font = "arial 15",
#                                     command = lambda: salir () )
# boton_2.grid (column = 0, row = 1)


# boton_1.bind("<Button-1>",un_click)
# boton_1.bind("<Double-1>",doble_click)
# # tamvien se puede hacer asi pero a la funsion ay que pasarle el parametro (event)
# boton_2.bind("<Button-1>",salir)


# Existen varios eventos a los que se pueden asociar funciones utilizando el método bind() en un widget de tkinter, además del evento <Button-1> utilizado en el ejemplo:
# <Button-1>: Se activa al hacer clic con el botón izquierdo del mouse.
# <Button-2>: Se activa al hacer clic con el botón central del mouse.
# <Button-3>: Se activa al hacer clic con el botón derecho del mouse.
# <Double-Button-1>: Se activa al hacer doble clic con el botón izquierdo del mouse.
# <Double-Button-2>: Se activa al hacer doble clic con el botón central del mouse.
# <Double-Button-3>: Se activa al hacer doble clic con el botón derecho del mouse.
# <Enter>: Se activa cuando el cursor del mouse entra en el área del widget.
# <Leave>: Se activa cuando el cursor del mouse sale del área del widget.
# <Return>: Se activa cuando se presiona la tecla Enter mientras el widget tiene el foco.
# <Key>: Se activa cuando se presiona cualquier tecla del teclado mientras el widget tiene el foco.
# <FocusIn>: Se activa cuando el widget recibe el foco.
# <FocusOut>: Se activa cuando el widget pierde el foco.

#------------------------------------------------------ventana para explorar archivos------------------------------------------------------------------------

# from tkinter import filedialog

# explorador_archivos = filedialog.askopenfilename()

#------------------------------------------------------paleta de colores---------------------------------------------------------------

# from tkinter import colorchooser

# colorchooser.askcolor(initialcolor = "#ffffff")



















ventana.mainloop()