import tkinter as tk

ventana = tk.Tk()

ventana.config (bg="black")
ventana.geometry("500x500")

seleccion = tk.IntVar()

def mostrar () :
    if seleccion.get() == 1 :
        Mensaje01 = "Elegistes Helado"
    if seleccion.get() == 2 :
        Mensaje01 = "Elegistes Torta de chocolate"
    if seleccion.get() == 3 :
        Mensaje01 = "Elegistes Alfajor de dulse de leche"
    
    Mensaje02.config(text=Mensaje01, fg="red", font="arial 15",)

def borrar () :
        seleccion.set(0)
        Mensaje01 = ""
        Mensaje02.config(text=Mensaje01, fg="red", font="arial 15",)

SBoton01 = tk.Radiobutton(ventana,  text="Helado",
                                    variable=seleccion,
                                    value=1,
                                    bg="blue" ,
                                    fg="red",
                                    font="arial 15",
                                    command=mostrar).place(x=10, y=10) 

SBoton02 = tk.Radiobutton(ventana,  text="Torta de chocolate",
                                    variable=seleccion,
                                    value=2,
                                    bg="blue" ,
                                    fg="red",
                                    font="arial 15", 
                                    command=mostrar).place(x=10, y=50) 

SBoton03 = tk.Radiobutton(ventana,  text="Alfajor de dulse de leche",
                                    variable=seleccion,
                                    value=3,
                                    bg="blue" ,
                                    fg="red", 
                                    font="arial 15",
                                    command=mostrar).place(x=10, y=90) 

boton = tk.Button(ventana,          text="resetiar selecsion",
                                    bg="blue" ,
                                    fg="red", 
                                    font="arial 15",
                                    command= borrar).place(x=10, y=170)

Mensaje02 = tk.Label(ventana,bg="blue")
Mensaje02.place(x=10, y=130)

ventana.mainloop()