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
                                    height="0"
                                    ).grid(padx= 10, pady=10)

def saludo ():
    tkinter.Label(ventana,  text="funcionara",
                            bg="red",                
                            fg="yellow"
                            ).grid(padx= 0, pady=0)

def crear_boton(tex,comand):
    return tkinter.Button(ventana,  text=tex,
                                    bg="blue",
                                    fg="red",
                                    command=comand,)



boton=crear_boton(   "prueva",saludo,)                               # cuando pongo boton en una variavle lo puedo volver a utilizar
boton.place(x=200, y=200, height=25 , width=200)                   

boton_02 = tkinter.Button(ventana,  text="salir",
                                    bg="red",
                                    fg="blue",
                                    command= ventana.destroy,
                                    ) .place(x=520, y=550, height=25 , width=50)




#   tkinter.messagebox.showinfo("cuidado" , "no te asustes")            #   te salta un cartel cuando lo abris
respuesta = tkinter.messagebox.askquestion ("????????", "te gusto")     #   te salta un cartel cuando lo abris con multiplea opsiones

if respuesta == "yes":
    tkinter.messagebox.showinfo ("","a mas te vale")
else:
    tkinter.messagebox.showinfo ("","como que no")





    # ventana.iconbitmap("form.ico")   #   Cambiar el icono. El icono que se muestra en la esquina superior izquierda se puede cambiar
    #                                   llamando el método iconbitmap, pasándole entre comillas doble el nombre de la imagen que debe
    #                                   estar con la extensión .ico y en el mismo lugar donde se tiene el programa. Por ejemplo se creo
    #                                   un icono con el nombre de form.ico.












ventana.mainloop()