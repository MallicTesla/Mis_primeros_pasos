import sqlite3

# conn = sqlite3.connect("C:\\Users\\Mallic\\Desktop\\Programas\\Mis_primeros_pasos\\Programacion\\002 ejemplos\\002 - 11 sqlite3\\primera_bace.db")
# c = conn.cursor()

# # ejecutar un SELECT en la tabla "stocks"
# c.execute("SELECT * FROM Estudiantes")

# numeros = [-1]
# for numero in numeros :
#     numero += 1
#     column_names = [name[numero] for name in c.fetchall()]


# rows = c.fetchall()


# c.execute("SELECT * FROM Estudiantes")
# table_contents = c.fetchall()

# print(column_names)

# # imprimir los resultados
# for row in table_contents:
#     print(row)


# c.close()


# conn.close()


# Conexión a la base de datos SQLite
conn = sqlite3.connect("C:\\Users\\Mallic\\Desktop\\Programas\\Mis_primeros_pasos\\Programacion\\002 ejemplos\\002 - 11 sqlite3\\primera_bace.db")

# Crear cursor
cursor = conn.cursor()

# Ejecutar consulta para obtener los nombres de las columnas
cursor.execute("PRAGMA table_info('Estudiantes')")
column_info = cursor.fetchall()
column_names = [col[1] for col in column_info]

# Ejecutar consulta para obtener los contenidos de la tabla
cursor.execute("SELECT * FROM Estudiantes")
table_contents = cursor.fetchall()

print(column_names)

# imprimir los resultados
for row in table_contents:
    print(row)


# Imprimir los nombres de las columnas y sus contenidos
print(column_names)
# print(table_contents)



# Cerrar la conexión y el cursor
cursor.close()
conn.close()