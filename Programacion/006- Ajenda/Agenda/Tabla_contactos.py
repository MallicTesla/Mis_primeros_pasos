import sqlite3
import Agenda.Base_de_datos as BD

def crear_tabla_contactos () :
    cursor = BD.abrir_base ()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Contactos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT,
    Apellido TEXT,
    Telefono TEXT,
    Email TEXT
    )""")

    cursor.close ()

def agregar (nuevo_contenido) :
    ruta_db = BD.crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    nuevo_contenido = nuevo_contenido.split (",")
    nuevo_contenido = tuple (nuevo_contenido)

    try :
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO Contactos (Nombre, Apellido, Telefono, Email) VALUES (?, ?, ?, ?)", nuevo_contenido)

        conn.commit()
        cursor.close()

    except sqlite3.ProgrammingError :
        conn.rollback()
        return True

def ver_contenido_Contactos () :
    ruta_db = BD.crear_ruta ()
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

def contacto_espesifico_linia (nuevo_contenido) :
    ruta_db = BD.crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    nuevo_contenido = nuevo_contenido.split (",")
    nuevo_contenido = tuple (nuevo_contenido)

    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Contactos WHERE Nombre=? AND Apellido=? AND Telefono=? AND Email=?", nuevo_contenido)
    if cursor.fetchone():
        return True

def contacto_espesifico_id (por_ID) :
    ruta_db = BD.crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Contactos WHERE id =?", (por_ID,))

    contacto = cursor.fetchone()
    if contacto is None :
        conn.close
        return True

    cursor.close ()
    conn.close

    return contacto

def borrar (borrar_ID) :
    if contacto_espesifico_id (borrar_ID) is True:
        return True

    ruta_db = BD.crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM Contactos WHERE id =?", (borrar_ID,))

    conn.commit ()
    cursor.close ()

    return False

def actualisar_fila (contenido_editado, por_ID) :
    contenido_editado = contenido_editado.split (",")
    contenido_editado = tuple (contenido_editado)

    ruta_db = BD.crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    cursor = conn.cursor()
    cursor.execute(f"UPDATE Contactos SET Nombre =?, Apellido =?, Telefono =?, Email =? WHERE id =?", contenido_editado + (por_ID,))

    conn.commit ()
    cursor.close ()