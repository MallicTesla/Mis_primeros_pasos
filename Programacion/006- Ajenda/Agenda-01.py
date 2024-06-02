import sqlite3
import os

def menu () :
    ruta_db = crear_ruta ()
    if not os.path.exists(ruta_db):
        print ("Creando base de datos ( agenda tabl-base de datoe.db )")
        crear_tabla_contactos ()
        crear_tabla_grupos ()
        crear_tabla_relasionamiento ()

    opsion = int (input ("""Que opsion queres realisar \n 1) Ver contactos \n 2) Agregar un contacto \n 3) Borrar contacto \n 4) Editar un Contacto 
5) Ver los nombres de los grupos existentes\n 6) Crear grupo \n 7) Editar el nombre de un grupo\n 8) Agregar un contacto a un grupo\n 9) Ver que contactos estan en un grupo
10) Ver a que grupos pertenese un contacto \nCualquier otra tecla para salir\n"""))

    match opsion :
        case 1 :
            print (f"Contactos \nID,Nomvre, Apellido, Telefono, Emeil\n{ver_contenido_Contactos()}")

        case 2 :
            print ("Agrega un nuevo contacto separado por , y si una columna va vacia se agrega un espasio y , menos si es la ultima\nNomvre, Apellido, Telefono, Emeil")
            nuevo_contenido = input ()

            agregar (nuevo_contenido)

        case 3 :
            print (f"Contactos \nID,Nomvre, Apellido, Telefono, Emeil\n{ver_contenido_Contactos ()}")
            borrar_ID = int (input ("Escrive el ID del contacto a borrar\n"))

            borrar (borrar_ID)

        case 4 :
            print(f"Contactos \nID,Nomvre, Apellido, Telefono, Emeil\n{ver_contenido_Contactos ()}")
            por_ID =  int (input ("Escrive el ID del contacto a editar\n"))
            contenido_editado = input ("Escriva el nuevo contacto separado por , y si una columna va vacia se agrega un espasio y , menos si es la ultima\nNomvre, Apellido, Telefono, Emeil\n")

            print (f"\nCambiastes a {contacto_espesifico_id (por_ID)}" )
            actualisar_fila (contenido_editado, por_ID)
            print (f"Por {contacto_espesifico_id (por_ID)} ")

        case 5 :
            print (f"Grupos :\nID  Nombre de los grupos\n{ver_contenido_Grupos()}")

        case 6 :
            print (f"Grupos existentes : \n{ver_contenido_Grupos ()}")
            nuevo_contenido = input ("Nombre del nuevo grupo :\n")

            grupo_nuevo (nuevo_contenido)

        case 7 :
            print (f"Grupos :\nID  Nombre de los grupos\n{ver_contenido_Grupos()}")
            por_ID = int (input("Elegir el ID del nombre del grupo a editar ID : "))
            contenido_editado = input ("Nuevo nombre :")

            print (f"\nCambiastes {nombre_grupo_id (por_ID)}")
            actualisar_fila_grupos (contenido_editado, por_ID)
            print (f"Por {nombre_grupo_id (por_ID)}")

        case 8 :
            print(f"Contactos \nID,Nomvre, Apellido, Telefono, Emeil\n{ver_contenido_Contactos ()}")
            Contacto_id = int (input ("Selecsionar el ID del contacto para agregarlo a un grupo : "))

            print (f"Grupos :\nID  Nombre de los grupos\n{ver_contenido_Grupos()}")
            Grupo_id = int (input("Selecsionar un ID de un grupo para agregarselo al contacto : "))

            relacionamiento_nuevo (Contacto_id, Grupo_id)

        case 9 :
            print (f"\nID  Nombre de los grupos\n{ver_contenido_Grupos()}")
            contactos_grupo = int (input ("Elegir el id del grupo a ver : "))

            print (f"En el grupo {nombre_grupo_id (contactos_grupo)[1]} se encuentran estos contactos")
            print (f"Contactos : \nID,Nomvre, Apellido, Telefono, Emeil\n{contactos_en_grupos (contactos_grupo)}")

        case 10 :
            print(f"Contactos \nID,Nomvre, Apellido, Telefono, Emeil\n{ver_contenido_Contactos ()}")
            grupos_contactos = int (input ("Elegir el id del contacto a ver : "))

            print (f"Este contacto {contacto_espesifico_id (grupos_contactos)}")
            print (f"Esta en estos grupos {grupos_en_contactos (grupos_contactos)}")

            ...
        case _: #esi seria el else del if
            ...

def crear_ruta ():
    # Obtener la ruta del directorio en el que se encuentra el archivo Python
    ruta_carpeta = os.path.dirname(os.path.abspath(__file__))

    # Construir la ruta relativa a la base de datos
    ruta_db = os.path.join(ruta_carpeta, "agenda tabl-base de datoe.db")

    # Crear la carpeta si no existe
    # if not os.path.exists(ruta_carpeta):
    #     os.makedirs(ruta_carpeta)

    return ruta_db

def abrir_base () :
    ruta_db = crear_ruta ()
    # Utilizar la ruta relativa para conectarse a la base de datos
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()
    return cursor

def crear_tabla_contactos () :
    cursor = abrir_base ()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Contactos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT,
    Apellido TEXT,
    Telefono TEXT,
    Email TEXT
    )""")

    cursor.close ()


def agregar (nuevo_contenido) :
    ruta_db = crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    nuevo_contenido = nuevo_contenido.split (",")
    nuevo_contenido = tuple (nuevo_contenido)

    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO Contactos (Nombre, Apellido, Telefono, Email) VALUES (?, ?, ?, ?)", nuevo_contenido)
    conn.commit()
    cursor.close()

def ver_contenido_Contactos () :
    ruta_db = crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Contactos")
    dicsionario = cursor.fetchall()

    lista_contenido = ""
    for lista in dicsionario :
        lista_contenido  += str (lista) + "\n"

    conn.commit ()
    cursor.close ()

    return lista_contenido

def contacto_espesifico_id (por_ID) :
    ruta_db = crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Contactos WHERE id =?", (por_ID,))

    contacto = cursor.fetchone()

    conn.commit ()
    cursor.close ()

    return contacto

def borrar (borrar_ID) :
    ruta_db = crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM Contactos WHERE id =?", (borrar_ID,))

    conn.commit ()
    cursor.close ()

def actualisar_fila (contenido_editado, por_ID) :
    contenido_editado = contenido_editado.split (",")
    contenido_editado = tuple (contenido_editado)

    ruta_db = crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    cursor = conn.cursor()
    cursor.execute(f"UPDATE Contactos SET Nombre =?, Apellido =?, Telefono =?, Email =? WHERE id =?", contenido_editado + (por_ID,))

    conn.commit ()
    cursor.close ()

#---------------------------------------------------------grupos---------------------------------------------------------------------------------

def crear_tabla_grupos () :
    ruta_db = crear_ruta ()
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Grupos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre_grupos TEXT)""")

    cursor.close ()
    conn.close ()

def ver_contenido_Grupos () :
    ruta_db = crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Grupos")
    dicsionario = cursor.fetchall()

    lista_contenido = ""
    for lista in dicsionario :
        lista_contenido  += str (lista) + "\n"

    conn.commit ()
    cursor.close ()

    return lista_contenido

def grupo_nuevo (nuevo_contenido) :
    ruta_db = crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    cursor = conn.cursor()
    cursor.execute("INSERT INTO Grupos (Nombre_grupos) VALUES (?)", (nuevo_contenido,))

    conn.commit()
    cursor.close()

def actualisar_fila_grupos (contenido_editado, por_ID) :
    ruta_db = crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    cursor = conn.cursor()
    cursor.execute(f"UPDATE Grupos SET Nombre_grupos =? WHERE id =?", (contenido_editado, por_ID,))

    conn.commit ()
    cursor.close ()

def nombre_grupo_id (por_ID) :
    ruta_db = crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Grupos WHERE id =?", (por_ID,))

    contacto = cursor.fetchone()

    conn.commit ()
    cursor.close ()

    return contacto

#----------------------------------------------------relasionamiento-------------------------------------------------------------------

def crear_tabla_relasionamiento () :
    ruta_db = crear_ruta ()
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Relacionamiento(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_Contactos INTEGER,
    id_Grupos INTEGER,
    FOREIGN KEY (id_Contactos) REFERENCES Contactos (id),
    FOREIGN KEY (id_Grupos) REFERENCES Grupos (id),
    UNIQUE (id_Contactos, id_Grupos))''')

    cursor.close()

def relacionamiento_nuevo (Contacto_id, Grupo_id) :
    ruta_db = crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    cursor = conn.cursor()
    cursor.execute("INSERT INTO Relacionamiento (id_Contactos, id_Grupos) VALUES (?, ?)", (Contacto_id, Grupo_id))
    

    conn.commit()
    cursor.close()

def contactos_en_grupos (contactos_grupo) :
    ruta_db = crear_ruta ()
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()

    cursor.execute (f'''
    SELECT DISTINCT c.id, c.Nombre, c.Apellido, c.Telefono, c.Email
    FROM Contactos c
    JOIN Relacionamiento re ON re.id_Contactos = c.id
    JOIN Grupos g ON g.id = re.id_Grupos
    WHERE g.id = {contactos_grupo}
''')
    resultados = cursor.fetchall()

    lista = ""
    for resultado in resultados:
        lista += str (resultado) + "\n"

    return lista

def grupos_en_contactos (grupos_contactos) :
    ruta_db = crear_ruta ()
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()

    cursor.execute('''
    SELECT DISTINCT g.Nombre_grupos
    FROM Grupos g
    JOIN Relacionamiento re ON re.id_Grupos = g.id
    JOIN Contactos c ON c.id = re.id_Contactos
    WHERE c.id = ?
    ''', (grupos_contactos,))

    resultados = cursor.fetchall()

    lista = ""
    for resultado in resultados:
        lista += str (resultado) + "\n"

    return lista

    ...






" Mia,Khalifa,098071091,MiaKhalifa@HOTmail.com "




menu ()


























