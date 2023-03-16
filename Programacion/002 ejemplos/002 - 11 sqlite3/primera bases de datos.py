import sqlite3

#    sqlite3.connect() asi se abre la bace de datos y la crea si no exixte tambien podes asignarle una ruta a la ruta ay que colocarle doble \\ sino da error
conn = sqlite3.connect("C:\\Users\\Mallic\\Desktop\\Programas\\Mis_primeros_pasos\\Programacion\\002 ejemplos\\002 - 11 sqlite3\\primera_bace.db")

#   el cursor es una variavle que va a tener unos datos en un momento determinado si se tienen muchos datos el cursor va ejecutando 1 por 1
cursor = conn.cursor()

#   execute es para hacer la una consulta a la base de datos
#   para crear una tabla se uasa CREATE TABLE nombre de la tabla, las triples comillas es para el salto de linea lo que esta en malluscula son comandos
#   entre (parentecic van los nombres de las columnas y el TIPO DE DATOS QUE SE ESPERA INGRESAR luego va una coma y la sigiente columna)
cursor.execute(""" CREATE TABLE IF NOT EXISTS Estudiantes(
    Matricula TEXT PRIMARI KEY,                      
    Nombre TEXT NOT NULL,
    Apellido TEXT NOT NULL,
    Promedio REAL)""")

#   CREATE TABLE se usa para crear una tabla seguida del nombre y el contenido (nombre de las columnas segida del comando la , se usa para ir a la sigiente columna)
#   el salto de linia no es nesesario es solo para que sea mas legible
#   TEXT        se usa para introdusir informasion de tipo string
#   REAL        se usa para introdusir informasion numerica
#   PRIMARI KEY se usa para que no se repita los datos de la columna

class Estudiantes :
    def __init__(self,matricula,nombre,apellido,promedio):
        self.matricula = matricula
        self.nombre = nombre
        self.apellido = apellido
        self.promedio = promedio

e_1 = Estudiantes ("112","Pablo","Nuñez",10)
e_2 = Estudiantes ("457","Sofia","Castillo",15)
e_3 = Estudiantes ("234","Andres","Velasquez",32)
e_4 = Estudiantes ("563","Ana","Gomez",27)
e_5 = Estudiantes ("781","Pedro","Mendez",9)
e_6 = Estudiantes ("986","Mariana","Lopez",44)

#   asi se escrive en la tabla 
# cursor.execute ("INSERT INTO Estudiantes VALUES ('111', 'Roverto', 'Carlos', 9.9)")
#   INSERT INTO se utiliza para insertar o agregar nuevos registros en una tabla existente
#   VALUES      se utiliza para especificar los valores que se insertarán en los campos correspondientes de la tabla

# cursor.execute ("INSERT INTO Estudiantes VALUES(?, ?, ?, ?)",(e_1.matricula, e_1.nombre, e_1.apellido, e_1.promedio))


#   para agregar todos los estudiantes se crea una tupla

many_estudiantes = [
(e_1.matricula, e_1.nombre, e_1.apellido, e_1.promedio),
(e_2.matricula, e_2.nombre, e_2.apellido, e_2.promedio),
(e_3.matricula, e_3.nombre, e_3.apellido, e_3.promedio),
(e_4.matricula, e_4.nombre, e_4.apellido, e_4.promedio),
(e_5.matricula, e_5.nombre, e_5.apellido, e_5.promedio),
(e_6.matricula, e_6.nombre, e_6.apellido, e_6.promedio)]



#   con executemany se puede agregar una lista 
cursor.executemany ("INSERT INTO Estudiantes VALUES(?, ?, ?, ?)", many_estudiantes)
#   commit se usa para guardar los cambios
conn.commit()

#------------------------------------------------------vista del contenido de la base de datos-------------------------------------------

#   SELECT * FROM   selecsionas todos los atributos de la lista

# cursor.execute("SELECT * FROM Estudiantes")
#   tambien se puede agregar WHERE para selecsionar una valor de una columna espesifica y que te de todos los datos de ese fila 
#   el valor que se le pide buscar tiene que ser una tupla vasta con poner una coma al final
cursor.execute("SELECT * FROM Estudiantes WHERE Matricula=?", ("112",))


#   con fetchall() crea un dicsionario de todos los alumnos
#   con fatchone() llama a un solo alumno
#   con fatchmany (cantidad)    pedis una cantidad X de alumnos
#   asi se ve el contenido de la base de datos
dicsionario = cursor.fetchall()
print (dicsionario)
for lista in dicsionario :
    print (lista)

cursor.close()      #   para cerar el cursor no es nesesario pero si lo es
conn.close()        #   asi se ciera la bace de datos