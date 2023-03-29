import sqlite3
import Agenda.Base_de_datos as BD

def crear_tabla_grupos () :
    ruta_db = BD.crear_ruta ()
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Grupos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre_grupos TEXT)""")

    cursor.close ()
    conn.close ()

def ver_contenido_Grupos () :
    try :
        ruta_db = BD.crear_ruta ()
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

    except sqlite3.ProgrammingError :
        conn.rollback()
        return True

def grupo_nuevo (nuevo_contenido) :
    ruta_db = BD.crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    cursor = conn.cursor()
    cursor.execute("INSERT INTO Grupos (Nombre_grupos) VALUES (?)", (nuevo_contenido,))

    conn.commit()
    cursor.close()

def actualisar_fila_grupos (contenido_editado, por_ID) :
    ruta_db = BD.crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    cursor = conn.cursor()
    cursor.execute(f"UPDATE Grupos SET Nombre_grupos =? WHERE id =?", (contenido_editado, por_ID,))

    conn.commit ()
    cursor.close ()

def grupo_espesifico_linia (nuevo_contenido) :
    ruta_db = BD.crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Grupos WHERE Nombre_grupos =?", (nuevo_contenido,))

    if cursor.fetchone():
        return True

    conn.commit ()
    cursor.close ()


def nombre_grupo_id (por_ID) :
    ruta_db = BD.crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Grupos WHERE id =?", (por_ID,))

    grupo = cursor.fetchone()

    if grupo is None :
        cursor.close ()
        conn.close
        return True

    cursor.close ()
    conn.close

    return grupo

def borrar_grupo (borrar_ID) :
    ruta_db = BD.crear_ruta ()
    conn = sqlite3.connect(ruta_db)

    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM Grupos WHERE id =?", (borrar_ID,))

    conn.commit ()
    cursor.close ()