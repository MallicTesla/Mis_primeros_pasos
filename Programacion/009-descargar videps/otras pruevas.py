# import tkinter as tk

# ventana = tk.Tk()
# ventana.title("Ejemplo de Cuadrícula")

# # Crear etiquetas y colocarlas en la cuadrícula
# etiqueta1 = tk.Label(ventana, text="Etiqueta 1")
# etiqueta2 = tk.Label(ventana, text="Etiqueta 2")
# etiqueta3 = tk.Label(ventana, text="Etiqueta 3")

# etiqueta1.grid(row=0, column=0)  # Fila 0, Columna 0
# etiqueta2.grid(row=1, column=1)  # Fila 1, Columna 1
# etiqueta3.grid(row=2, column=2)  # Fila 2, Columna 2

# # Crear un botón y colocarlo en la cuadrícula
# boton = tk.Button(ventana, text="Botón")
# boton.grid(row=3, column=1)  # Fila 3, Columna 1

# ventana.mainloop()


import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de Cuadrícula con 3 Columnas")

# Crear etiquetas y colocarlas en la cuadrícula
etiqueta1 = tk.Label(ventana, text="Etiqueta 1")
etiqueta2 = tk.Label(ventana, text="Etiqueta 2")
etiqueta3 = tk.Label(ventana, text="Etiqueta 3")

etiqueta1.grid(row=0, column=0)  # Fila 0, Columna 0
etiqueta2.grid(row=1, column=1)  # Fila 1, Columna 1
etiqueta3.grid(row=2, column=2)  # Fila 2, Columna 2

# Crear un botón y colocarlo en la cuadrícula
boton = tk.Button(ventana, text="Botón")
boton.grid(row=3, column=1, columnspan=2)  # Fila 3, Columna 1, se extiende a 2 columnas

ventana.mainloop()