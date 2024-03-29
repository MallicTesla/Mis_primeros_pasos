import Agenda.Tabla_contactos as TC
import Agenda.Tabla_grupos as TG
import Agenda.Tabla_relasionamiento as TR
import sqlite3
import os

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

def primera_vez () :
    ruta_db = crear_ruta ()
    if not os.path.exists(ruta_db):
        TC.crear_tabla_contactos ()
        TG.crear_tabla_grupos ()
        TR.crear_tabla_relasionamiento ()

    return False