from tkinter import *
from tkinter import ttk

ventana = Tk ()
ventana.title("Primera Ventana")    #   Cambiar el nombre de la ventana
ventana.geometry("520x480")         #   Configurar tamaño
ventana.resizable(1,1)              #   para modificar manual mente el tamaño (para no modificarla(0,0)) (para modificarlo(1,1))
ventana.config(bg="#500090") 
frm = ttk.Frame(ventana, padding=10)
frm.grid()
ttk.Label(frm, text="funcionara").grid(column=0, row=0)
ttk.Button(frm, text="Quitar", command=ventana.destroy).grid(column=1, row=0)






ventana.mainloop()