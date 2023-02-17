import tkinter as tk

ventana=tk.Tk()

ventana.title("Primera Ventana")    
ventana.geometry("600x600")
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
                                    justify="center",
                                    font= "roman 15 bold",)
Mensaje05.place(x=10, y=220)

class test ():
    def __init__(self):
        self.ventana = tk.Tk ()
        # tenemos que crear una variavle de tipo StringVar para cambiar el texto de un widget
        self.texto01 = tk.StringVar()
        # le damos un valor inicial
        self.texto01.set ("Es mi primera ves")

        # creamos la etiqueta
        # con textcariavle indicamos cual es la variavle que tendra el texto 
        self.Etiqueta01 = tk.Label(self.ventana,    textovariavle = self.texto01,
                                                    font= "arial 20").pack()
        
        # creamos el boton 
        self.boton01 = tk.Button(self.ventana,  text="Vos tranqui",
                                                font="arial 20 ",
                                                command=self.changeText).pack()
        
        self.ventana.mainloop()


    # este metodo es el handLer
    def changeTexto(self):
        pass





# imgagen01 = tk.PhotoImage(file="imagen001.png" )

# Mensaje01 = tk.Label(ventana,   image=imgagen01) .pack(side="right")  #   side=   es para posisionar la imagen

# texto02 = """asi se coloca un texto 
# alado de una imagen"""

# Mensaje02 = tk.Label(ventana,   text=texto02).pack(side="left")

# texto03 = """y asi es para colocarlo un 
# texto encima de una imajen"""

# Mensaje03 = tk.Label(ventana,   text=texto03,
#                                 image=imgagen01,
#                                 compound=tk.CENTER). pack()









ventana.mainloop()