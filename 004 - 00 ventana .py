import  tkinter
ventana = tkinter.Tk ()
ventana.title("Primera Ventana")    #   Cambiar el nombre de la ventana
ventana.geometry("520x480")         #   Configurar tamaño
ventana.resizable(1,1)              #   para modificar manual mente el tamaño (para no modificarla(0,0)) (para modificarlo(1,1))
ventana.config(bg="#500090")        #   Cambiar color de fond el color en inglés o en formato hexadecima
cabezera = tkinter.Label(ventana,   fg="yellow",
                                    bg="red" ,
                                    height="10", 
                                    text="    vamos a ver si funciona     " ).grid(column=0, row=0)






    # ventana.iconbitmap("form.ico")   #   Cambiar el icono. El icono que se muestra en la esquina superior izquierda se puede cambiar
    #                                   llamando el método iconbitmap, pasándole entre comillas doble el nombre de la imagen que debe
    #                                   estar con la extensión .ico y en el mismo lugar donde se tiene el programa. Por ejemplo se creo
    #                                   un icono con el nombre de form.ico.












ventana.mainloop()