import Agenda.Base_de_datos as BD
import Agenda.Tabla_contactos as TC
import Agenda.Tabla_grupos as TG
import Agenda.Tabla_relasionamiento as TR
import os

def menu () :
    while True :
        ruta_db = BD.crear_ruta ()
        if not os.path.exists(ruta_db):
            print ("Creando base de datos ( agenda tabl-base de datoe.db )")
            TC.crear_tabla_contactos ()
            TG.crear_tabla_grupos ()
            TR.crear_tabla_relasionamiento ()

        opsion = input ("Que te gustaria ver : \n1) Contactos \n2) Grupos \nPrecione cualquier tecla para salir\n")

        match opsion :
            case "1" :
                while True :
                    opsion = input ("Que opsion queres realisar \n1) Agregar un contacto \n2) Ver contactos  \n3) Borrar contacto \n4) Editar un Contacto \nPrecione cualquier tecla para regresar\n")

                    match opsion :

                        case "1" :
                            while True :
                                print(f"Contactos ya existentes \nID,Nomvre, Apellido, Telefono, Emeil\n{TC.ver_contenido_Contactos()}")
                                print ("Agrega un nuevo contacto separado por , y si una columna va vacia se agrega un espasio y , menos si es la ultima\nNomvre, Apellido, Telefono, Emeil")
                                nuevo_contenido = input ()

                                TC.agregar (nuevo_contenido)

                                de_donde = "agregar otro contacto"
                                if regresar (de_donde) :
                                    break

                        case "2" :
                            print(f"Contactos \nID,Nomvre, Apellido, Telefono, Emeil\n{TC.ver_contenido_Contactos()}")

                        case "3" :
                            while True :
                                print(f"Contactos \nID,Nomvre, Apellido, Telefono, Emeil\n{TC.ver_contenido_Contactos ()}")
                                borrar_ID = int (input ("Escrive el ID del contacto a borrar\n"))

                                TC.borrar (borrar_ID)

                                de_donde = "borrar otro contacto"
                                if regresar (de_donde) :
                                    break

                        case "4" :
                            while True :
                                print(f"Contactos \nID,Nomvre, Apellido, Telefono, Emeil\n{TC.ver_contenido_Contactos ()}")
                                por_ID =  int (input ("Escrive el ID del contacto a editar\n"))
                                contenido_editado = input ("Escriva el nuevo contacto separado por , y si una columna va vacia se agrega un espasio y , menos si es la ultima\nNomvre, Apellido, Telefono, Emeil\n")

                                print (f"\nCambiastes a {TC.contacto_espesifico_id (por_ID)}" )
                                TC.actualisar_fila (contenido_editado, por_ID)
                                print (f"Por {TC.contacto_espesifico_id (por_ID)} \n")

                                de_donde = "editar otro contacto"
                                if regresar (de_donde) :
                                    break

                        case _ :
                            break

            case "2" :
                while True :
                    opsion = input ("""1) Crear grupo\n2) Ver los nombres de los grupos existentes \n3) Editar el nombre de un grupo \n4) Borar un grupo \n5) Agregar un contacto a un grupo 
6) Ver que contactos estan en un grupo \n7) Ver a que grupos pertenese un contacto \n8) Eliminar a un contacto de un grupo \nPrecione cualquier tecla para regresar\n""")

                    match opsion :
                        case "1" :
                            while True :
                                print (f"Grupos existentes : \n{TG.ver_contenido_Grupos ()}")
                                nuevo_contenido = input ("Nombre del nuevo grupo :\n")

                                TG.grupo_nuevo (nuevo_contenido)

                                de_donde = "crear otro grupo"
                                if regresar (de_donde) :
                                    break

                        case "2" :
                            print (f"Grupos :\nID  Nombre de los grupos\n{TG.ver_contenido_Grupos()}")

                        case "3" :
                            while True :
                                print (f"Grupos :\nID  Nombre de los grupos\n{TG.ver_contenido_Grupos()}")
                                por_ID = int (input("Elegir el ID del nombre del grupo a editar ID : "))
                                contenido_editado = input ("Nuevo nombre :")

                                print (f"\nCambiastes {TG.nombre_grupo_id (por_ID)}")
                                TG.actualisar_fila_grupos (contenido_editado, por_ID)
                                print (f"Por {TG.nombre_grupo_id (por_ID)}\n")

                                de_donde = "editar otro grupo"
                                if regresar (de_donde) :
                                    break

                        case "4" :
                            while True :
                                print(f"ID  Nombre de los grupos\n{TG.ver_contenido_Grupos ()}")
                                borrar_ID = int (input ("Escrive el ID del grupo a borrar\n"))

                                TG.borrar_grupo (borrar_ID)

                                de_donde = "borrar otro grupo"
                                if regresar (de_donde) :
                                    break

                        case "5" :
                            while True :
                                print(f"Contactos \nID,Nomvre, Apellido, Telefono, Emeil\n{TC.ver_contenido_Contactos ()}")
                                Contacto_id = int (input ("Selecsionar el ID del contacto para agregarlo a un grupo : "))

                                print (f"Grupos :\nID  Nombre de los grupos\n{TG.ver_contenido_Grupos()}")
                                Grupo_id = int (input("Selecsionar un ID de un grupo para agregarselo al contacto : "))

                                TR.relacionamiento_nuevo (Contacto_id, Grupo_id)

                                de_donde = "agregar a otro contacto a otro grupo"
                                if regresar (de_donde) :
                                    break

                        case "6" :
                            while True :
                                print (f"\nID  Nombre de los grupos\n{TG.ver_contenido_Grupos()}")
                                contactos_grupo = int (input ("Elegir el id del grupo a ver : "))

                                print (f"En el grupo {TG.nombre_grupo_id (contactos_grupo)[1]} se encuentran estos contactos")
                                print (f"Contactos : \nID,Nomvre, Apellido, Telefono, Emeil\n{TR.contactos_en_grupos (contactos_grupo)}")

                                de_donde = "ver otro grupo"
                                if regresar (de_donde) :
                                    break

                        case "7" :
                            while True :
                                print(f"Contactos \nID,Nomvre, Apellido, Telefono, Emeil\n{TC.ver_contenido_Contactos ()}")
                                grupos_contactos = int (input ("Elegir el id del contacto a ver : "))

                                print (f"Este contacto {TC.contacto_espesifico_id (grupos_contactos)}")
                                print (f"Esta en estos grupos {TR.grupos_en_contactos (grupos_contactos)}")

                                de_donde = "ver otro contacto"
                                if regresar (de_donde) :
                                    break

                        case "8" :
                            while True :
                                print (f"Eliga el ID del contacto y despues el ID del grupo\n")

                                print(f"Contactos : \nID,Nomvre, Apellido, Telefono, Emeil\n{TC.ver_contenido_Contactos ()}")
                                contacto_id = int (input("elegir el ID del contacto : "))

                                print(f"ID  Nombre de los grupos\n{TG.ver_contenido_Grupos ()}")
                                grupo_id = int (input("Elegir el ID del grupo : "))

                                TR.desrelacionar_contacto_grupo(contacto_id, grupo_id)

                                de_donde = "eliminar a otro contacto de otro grupo"
                                if regresar (de_donde) :
                                    break

                        case _ :
                            break

            case _ :
                print ("Adios")
                break

def regresar (de_donde) :
    opsion = input (f"Decea {de_donde} 1) Si 2) No\n")
    if opsion == "1" :
        return False
    else :
        return True

menu ()