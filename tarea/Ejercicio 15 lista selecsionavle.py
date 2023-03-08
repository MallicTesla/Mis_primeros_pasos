import tkinter as tk

ventana = tk.Tk()

lista = ["Pan","Queso","Mayonesa","Lechuga","Jamon","Pimienta","Jamon","Tomate","Queso","Pan"]
lista_items = tk.StringVar(value = lista)

lista = tk.Listbox (ventana,height = 10, font="arial 15", listvariable = lista_items) .pack()

mensaje = tk.Label(ventana, text="y asi esta compuesto un sandwiches", font="arial 15").pack()

ventana.mainloop()