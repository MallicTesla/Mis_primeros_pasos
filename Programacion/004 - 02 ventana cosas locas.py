import tkinter
import tkinter.messagebox           #   parte de una libreria de tk
ventana = tkinter.Tk ()
ventana.title("Primera Ventana")    #   Cambiar el nombre de la ventana
ventana.geometry("600x600")         #   Configurar tamaño
ventana.resizable(1,1)              #   para modificar manual mente el tamaño (para no modificarla(0,0)) (para modificarlo(1,1))
ventana.config(bg="#500090")        #   Cambiar color de fond el color en inglés o en formato hexadecima

cabezera = tkinter.Label(ventana,   text="    vamos a ver si funciona     ",
                                    bg="red" ,
                                    fg="yellow", 
                                    height="0",
                                    ).grid(padx= 10, pady=10)

def reparando (n):
    tkinter.messagebox.askquestion ("????????",f"numero {n}")
    print (n)

lista=[1,2,3,4,5,]
for numero in lista :

    tkinter.Button(ventana,         text=f"numero {numero}",
                                    bg="green",
                                    fg="black",
                                    command= lambda:reparando(numero),
                                    ) .place(x=520, y=numero*30,)


print(numero)
























ventana.mainloop()