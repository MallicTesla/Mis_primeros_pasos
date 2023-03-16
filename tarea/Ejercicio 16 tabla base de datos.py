import sqlite3

conn = sqlite3.connect ("C:\\Pruebas\\base de datos\\Ejercisio16.db")

def crear_tabla () :
    cursor = conn.cursor()

    cursor.execute(""" CREATE TABLE IF NOT EXISTS Alumnos(
        Id INTEGER,                      
        Nombre TEXT,
        apellido TEXT)""")
    
    cursor.close

class Estudiantes :
    def __init__(self,Id,nombre,apellido):
        self.Id = Id 
        self.nombre = nombre
        self.apellido = apellido

e_1 = Estudiantes (0,"Pablo","Nuñez")
e_2 = Estudiantes (1,"Sofia","Castillo")
e_3 = Estudiantes (2,"Andres","Velasquez")
e_4 = Estudiantes (3,"Ana","Gomez")
e_5 = Estudiantes (4,"Pedro","Mendez")
e_6 = Estudiantes (5,"Mariana","Lopez")
e_7 = Estudiantes (6,"Mariana","Lopez")
e_8 = Estudiantes (7,"Mariana","Lopez")

many_estudiantes = [
(e_1.Id, e_1.nombre, e_1.apellido),
(e_2.Id, e_2.nombre, e_2.apellido),
(e_3.Id, e_3.nombre, e_3.apellido),
(e_4.Id, e_4.nombre, e_4.apellido),
(e_5.Id, e_5.nombre, e_5.apellido),
(e_6.Id, e_6.nombre, e_6.apellido),
(e_7.Id, e_7.nombre, e_7.apellido),
(e_8.Id, e_8.nombre, e_8.apellido)]

nombres =[
(e_1.nombre),
(e_2.nombre),
(e_3.nombre),
(e_4.nombre),
(e_5.nombre),
(e_6.nombre),
(e_7.nombre),
(e_8.nombre),]

def agregar_estudiantes (mis_estudiantes) :
    cursor = conn.cursor()
    cursor.executemany ("INSERT INTO Alumnos VALUES(?, ?, ?)", mis_estudiantes)

    conn.commit()
    cursor.close

def ver_columnas (tabla) :
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({tabla})")
    columna_info = cursor.fetchall()
    titulo_columnas = [col[1] for col in columna_info]

    cursor.close

    return titulo_columnas

def ver_contenido (tabla) :
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {tabla}")
    dicsionario = cursor.fetchall()

    lista_contenido = ""
    for lista in dicsionario :
        lista_contenido  += str (lista) + "\n"

    cursor.close ()

    return lista_contenido

def buscar (nombre_alumno) :
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Alumnos WHERE nombre=?", (f"{nombre_alumno}",))
    estudiante_selecsionado = cursor.fetchone()

    cursor.close ()

    return estudiante_selecsionado

def menu () :
    while True :
        opcion = int (input("que operacion deseas realisar \n1) crear tabla \n2) Insertar estudiantes \n3) Buscar estudiante por nombre \n4) Salir\n"))

        if opcion == 1 :
            crear_tabla()
            print ("Ya se creo la tabla\n")

        elif opcion == 2 :
            agregar_estudiantes (many_estudiantes)
            print ("Se agregaron los sigientes estudiantes :\n",ver_contenido(tabla))

        elif opcion == 3 :
            print (f"Nombres de los alumnos\n{nombres}\n")
            nombre_alumno = input ("colocar el nombre del estudiante a buscar : ")
            print (f"{ver_columnas (tabla)}\n{buscar(nombre_alumno)}")

        else : 
            break

tabla = "Alumnos"

menu ()

conn.close