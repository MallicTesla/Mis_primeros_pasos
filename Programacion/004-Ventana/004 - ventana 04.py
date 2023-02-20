import tkinter as tk

ventana=tk.Tk()
seleccion = tk.IntVar()

ventana.title("Primera Ventana")    
ventana.geometry("1000x1000")
ventana.resizable(1,1)
ventana.config(bg="#500090") 

texto01 = """espro que ahora si
funcione esto"""

cabezera = tk.Label(ventana,        text=texto01,
                                    bg="red" ,
                                    fg="yellow", 
                                    height="0",
                                    width= "0",                          #   para ajustar el ancho
                                    justify="left",                    #   Para posisionar el testo dentro de la etiqueta (justify = left , center , right)
                                    font= "italic 10 bold",              #   para cambiar el tipo de letra y el tamaño ,bold es para aserlas mas gruesas
                                    ).grid(padx= 10, pady=10)

cabezera2 = tk.Label(ventana,       text="Provando otras letras",
                                    bg="red" ,
                                    fg="yellow", 
                                    height="0",
                                    justify="center",
                                    font= "roman 15 bold",                                    
                                    ).place(x=10, y=55) 

texto04 = "vamos a ver si logro hacer que este texto aparesca en multiples rengloses de forma automatica sin que lo aga manualmente en la variavle"

Mensaje04= tk.Message(ventana,      text= texto04,
                                    width= 300,                    #    para ajustar el ancho de las columnas no se puede ajustar el alto
                                    bg="blue" ,
                                    fg="orange", 
                                    justify="center",
                                    font= "roman 15 bold",                                    
                                    ).place(x=10, y=90) 

texto05 = "con el comando (variavle.config()) se puede agregar mas configuraciones a una variable existente y en otro renglon se coloca las cordenadas(Mensaje04.place(x=10, y=270) )"

Mensaje05= tk.Message(ventana,      text= texto05)
Mensaje05.config(                   width= 300,
                                    bg="green" ,
                                    fg="yellow", 
                                    justify="left",
                                    font= "roman 15 bold",)
Mensaje05.place(x=10, y=220)
#---------------------------boton que remplasa un texto en el wifget------------------------------------------------
class test ():
    def __init__(self):
        # tenemos que crear una variavle de tipo StringVar para cambiar el texto de un widget
        self.texto06 = tk.StringVar()
        # le damos un valor inicial
        self.texto06.set ("Es mi primera ves")
        # creamos la etiqueta
        # con textcariavle indicamos cual es la variavle que tendra el texto 
        self.Etiqueta01 = tk.Label(ventana,     textvariable = self.texto06,
                                                font= "arial 15").place(x=10, y=400)        
        # creamos el boton 
        self.boton01 = tk.Button(ventana,       text="Vos tranqui",
                                                font="arial 15 ",
                                                command=self.texto07
                                                ).place(x=10, y=440)    #   lo que ace el boton
        
        ventana.mainloop()

    # este metodo es el handLer
    def texto07(self):
        self.texto06.set("te pensas que eso me va a calmar")

#--------------------radio boton----------------------------------------------------

def mostrar () :                                                #   .get() se usa para leer el contenido de la variavle
    if seleccion.get() == 1 :
        Mensaje06 = "boton 1"
    if seleccion.get() == 2 :
        Mensaje06 = "boton 2"
    if seleccion.get() == 3 :
        Mensaje06 = "boton 3"
    
    Mensaje07.config(text=Mensaje06)

SBoton01 = tk.Radiobutton(ventana,  text="boton 1",
                                    variable=seleccion,
                                    value=1,
                                    bg="blue" ,
                                    fg="orange", 
                                    command=mostrar).place(x=350, y=10) 

SBoton02 = tk.Radiobutton(ventana,  text="boton 2",
                                    variable=seleccion,
                                    value=2,
                                    command=mostrar).place(x=350, y=35) 

SBoton03 = tk.Radiobutton(ventana,  text="boton 3",
                                    variable=seleccion,
                                    value=3,
                                    command=mostrar).place(x=350, y=60) 

Mensaje07 = tk.Label(ventana)
Mensaje07.place(x=350, y=85) 

#-----------------------check botton-------------------------------------

def FCheck (): 
    Mensaje08 = " "

    if (check01.get() == 1) :
        Mensaje08 = Mensaje08 + "check 01"    
    
    if (check02.get() == 1) :
        Mensaje08 = Mensaje08 + "check 02"

    if check01.get() != check02.get():
        Mensaje08 = Mensaje08 + " podes elegir otro"


    Mensaje09.config(text = Mensaje08)
    

#   esta variavle se usa para conoser los estados de los check box

check01 = tk.IntVar()
check02 = tk.IntVar()

#   etiqueta para mostrar el mensaje
Mensaje09 = tk.Label(ventana)
Mensaje09.place(x=350, y=195) 

#   creamos los check box
TexCheck01= tk.Checkbutton(ventana, text="Check boton 1",
                                    variable=check01,
                                    ).place(x=350, y=115) 

TexCheck02= tk.Checkbutton(ventana, text="Check boton 2",
                                    variable=check02,
                                    ).place(x=350, y=140) 

#   boton para llevar a cabo la acccion de la funcion FCheck

BoFCheck = tk.Button(ventana,   text=" elegi uno o mas",
                                command=FCheck,
                                ).place(x=350, y=166)

#-----------------------------





imgagen01 = tk.PhotoImage(file="C:\imagen002.gif" )

Mensaje01 = tk.Label(ventana,   image=imgagen01) 
Mensaje01.place(x=350, y=166)                #   side=   es para posisionar la imagen

# texto02 = """asi se coloca un texto 
# alado de una imagen"""

# Mensaje02 = tk.Label(ventana,   text=texto02).pack(side="left")

# texto03 = """y asi es para colocarlo un 
# texto encima de una imajen"""

# Mensaje03 = tk.Label(ventana,   text=texto03,
#                                 image=imgagen01,
#                                 compound=tk.CENTER). pack()







app = test()

ventana.mainloop()