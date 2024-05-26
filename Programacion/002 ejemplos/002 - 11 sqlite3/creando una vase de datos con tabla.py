import sqlite3

conn = sqlite3.connect("C:\\Users\\Mallic\\Desktop\\Programas\\Mis_primeros_pasos\\Programacion\\002 ejemplos\\002 - 11 sqlite3\\tabla.db")

def menu () :
    opsion = int (input ("Que opsion queres realisar \n1) Creear una tabla \n2) Ver una tablas y editarla \n3) Borrar una tabla\n"))
    
    if opsion == 1 :
        print (f"Tablas ya existentes {ver_tablas ()}")
        nombre_tabla = input ("Nombre de la tabla\n")
        nombre_columna = input ("Coloca el titulo de cada columna seperada por ,\n")
        nombre_columna = nombre_columna.split (",")
        print (f"La tabla se llama : {nombre_tabla} \nLos titulos de las columnas son : {nombre_columna}")
        columnas = crear_columnas (nombre_columna)
        crear(nombre_tabla, columnas)

        menu()
    
    elif opsion == 2 :
        ver_una_tabla_y_editarla ()

    elif opsion == 3 :
        print (f"Que tabla deseas eliminar {ver_tablas()}")
        eliminar_tabla = input ()
        borrar_tabla (eliminar_tabla)

        menu()

def ver_una_tabla_y_editarla () :
    print (ver_tablas ())
    tabla_selecsionada = input ("De cual\n")

    columnas = ver_columnas (tabla_selecsionada)
    contenido = ver_contenido (tabla_selecsionada)

    print (columnas)
    print (contenido)

    while True :
        quiero2 = int (input("1) Agregar contenido \n2) Borar contenido de una fila \n3) Ver otra tabla \n4) Realisar otra operasion \n5) Salir\n"))

        if quiero2 == 1 :
            print ("Agregar contenido cada columna separarla con , y si una columna esta vacia colocar un espasio y , menos si es la ultima\n",columnas,"\n",ver_contenido(tabla_selecsionada))
            nuevo_contenido = input ()
            agregar (tabla_selecsionada, nuevo_contenido)

        elif quiero2 == 2 :
            print (f"escriva un VALOR de la fila que quiera borar y la columna en la que se encuentra ese valor.\n {columnas}\n{ver_contenido(tabla_selecsionada)}")
            borrar_fila = input ("Valor de la fila : ")
            borrar_columna = input ("Columna : ")
            

            borrar (tabla_selecsionada, borrar_columna, borrar_fila)

        elif quiero2 == 3 :
            ver_una_tabla_y_editarla ()

        elif quiero2 == 4 :
            menu ()

        else :
            break



def crear (nombre_tabla, columnas) :
    cursor = conn.cursor()

    cursor.execute (f"CREATE TABLE IF NOT EXISTS {nombre_tabla}({columnas})")

    cursor.close

def crear_columnas (nombre_columna) :

    columnas = [nombre + " TEXT" for nombre in nombre_columna]
    # print (columnas)
    return ",".join(columnas)


def ver_tablas ():
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    nombres_tablas = [tabla[0] for tabla in cursor.fetchall()]

    cursor.close()

    return nombres_tablas

def ver_columnas (este) :
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({este})")
    columna_info = cursor.fetchall()
    titulo_columnas = [col[1] for col in columna_info]
    
    # print (titulo_columnas)
    
    return titulo_columnas

def ver_contenido (este) :
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {este}")
    dicsionario = cursor.fetchall()

    lista_contenido = ""
    for lista in dicsionario :
        lista_contenido  += str (lista) + "\n"
    
    # print ("3", lista_contenido)

    conn.commit ()
    cursor.close ()

    return lista_contenido

def agregar (tabla_selecsionada, nuevo_contenido) :
    nuevo_contenido = nuevo_contenido.split (",")
    nuevo_contenido = tuple (nuevo_contenido)

    cursor = conn.cursor()
    cursor.execute (f"INSERT INTO {tabla_selecsionada} VALUES {nuevo_contenido}")
    conn.commit()
    cursor.close()

def borrar (tabla_selecsionada, borrar_columna, borrar_fila) :
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {tabla_selecsionada} WHERE {borrar_columna} =?", (borrar_fila,))
    conn.commit ()
    cursor.close ()

def borrar_tabla (eliminar_tabla) :
    cursor = conn.cursor()
    cursor.execute (f"DROP TABLE {eliminar_tabla} ")

    conn.commit ()
    cursor.close ()

menu ()

conn.close() 