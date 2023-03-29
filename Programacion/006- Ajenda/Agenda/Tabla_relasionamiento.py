import sqlite3
import Agenda.Base_de_datos as BD

def crear_tabla_relasionamiento () :
    ruta_db = BD.crear_ruta ()
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Relacionamiento(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_Contactos INTEGER,
    id_Grupos INTEGER,
    FOREIGN KEY (id_Contactos) REFERENCES Contactos (id),
    FOREIGN KEY (id_Grupos) REFERENCES Grupos (id),
    UNIQUE (id_Contactos, id_Grupos))''')

    conn.close()
    cursor.close()

def relacionamiento_nuevo (Contacto_id, Grupo_id) :
    ruta_db = BD.crear_ruta ()
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()

    try :
        cursor.execute("INSERT INTO Relacionamiento (id_Contactos, id_Grupos) VALUES (?, ?)", (Contacto_id, Grupo_id))
        conn.commit()

        cursor.close()
        conn.close()
        return False

    except sqlite3.IntegrityError:
        cursor.close()
        conn.close()
        return True



def contactos_en_grupos (contactos_grupo) :
    ruta_db = BD.crear_ruta ()
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
    ruta_db = BD.crear_ruta ()
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()

    cursor.execute('''
    SELECT DISTINCT g.id, g.Nombre_grupos
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

def desrelacionar_contacto_grupo(contacto_id, grupo_id):
    ruta_db = BD.crear_ruta()
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Relacionamiento WHERE id_Contactos = ? AND id_Grupos = ?', (contacto_id, grupo_id))

    if cursor.fetchone() is None:
        cursor.close ()
        conn.close
        return True

    else :
        cursor.execute('DELETE FROM Relacionamiento WHERE id_Contactos = ? AND id_Grupos = ?', (contacto_id, grupo_id))
        conn.commit()

        cursor.close()
        conn.close()
        return False