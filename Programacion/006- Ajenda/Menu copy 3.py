import Agenda.Base_de_datos as BD
import Agenda.Tabla_contactos as TC
import Agenda.Tabla_grupos as TG
import Agenda.Tabla_relasionamiento as TR

def menu () :
    while True :
        if BD.primera_vez () :
            print ("Creando base de datos ( agenda tabl-base de datoe.db )")

        opsion = input ("Que te gustaria ver : \n1) Contactos \n2) Grupos \nPrecione cualquier tecla para salir\n")

        match opsion :
            case "1" :
                while True :
                    opsion = input ("Que opsion queres realisar \n1) Agregar un contacto \n2) Ver contactos  \n3) Borrar contacto \n4) Editar un Contacto \nPrecione cualquier tecla para regresar\n")

                    match opsion :

                        case "1" :
                            while True :
                                print (f"Contactos ya existentes \nID,Nomvre, Apellido, Telefono, Emeil\n{TC.ver_contenido_Contactos()}")
                                print ("Agrega un nuevo contacto separado por , y si una columna va vacia se agrega un espasio y , menos si es la ultima\nNomvre, Apellido, Telefono, Emeil")
                                nuevo_contenido = input ()

                                if TC.contacto_espesifico_linia (nuevo_contenido) :
                                    print ("\nEse contacto ya esta registrado\n")

                                else :
                                    if TC.agregar(nuevo_contenido) :
                                        print (f"\n{nuevo_contenido} no cumple con las condisiones espesificadas")
                                        print ("""Hubo un error al rellenar las columnas asegurate de que esten todas las columnas con contenido y separadas por una , 
y si una columna va vacia se agrega un espasio y , menos si es la ultima recuerda que tenes que tener 3 , en total \n """)

                                de_donde = "agregar otro contacto"
                                if regresar (de_donde) :
                                    break

                        case "2" :
                            print(f"Contactos \nID,Nomvre, Apellido, Telefono, Emeil\n{TC.ver_contenido_Contactos()}")

                        case "3" :
                            while True :
                                print(f"Contactos \nID,Nomvre, Apellido, Telefono, Emeil\n{TC.ver_contenido_Contactos ()}")
                                mensaje = "Escrive el ID del contacto a borrar\n"
                                borrar_ID = si_nummeros (mensaje)

                                if TC.contacto_espesifico_id(borrar_ID) is True :
                                    print (f"El ID seleccionar ({borrar_ID}) no existe verifique el ID")

                                else :
                                    print (f"Seguro que quieres borar a : \n{TC.contacto_espesifico_id(borrar_ID)}\n1) Si \n2) No")
                                    seguro = input ()

                                    if seguro == "1" :
                                        if TC.borrar (borrar_ID) :
                                            print (f"El ID seleccionar ({borrar_ID}) no existe verifique el ID")

                                de_donde = "borrar otro contacto"
                                if regresar (de_donde) :
                                    break

                        case "4" :
                            while True :
                                print(f"Contactos \nID,Nomvre, Apellido, Telefono, Emeil\n{TC.ver_contenido_Contactos ()}")
                                mensaje = "Escrive el ID del contacto a borrar\n"
                                por_ID = si_nummeros (mensaje)
                                contenido_editado = input ("Escriva el nuevo contacto separado por , y si una columna va vacia se agrega un espasio y , menos si es la ultima\nNomvre, Apellido, Telefono, Emeil\n")

                                if TC.contacto_espesifico_id(por_ID) is True :
                                        print (f"El ID seleccionar ({por_ID}) no existe verifique el ID")
                                
                                else :
                                    print (f"Seguro que quieres cambiar a : \n{TC.contacto_espesifico_id(por_ID)}\n1) Si \n2) No")
                                    seguro = input ()

                                    if seguro == "1" :
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
                    opsion = input ("""1) Crear grupo\n2) Ver los nombres de los grupos existentes \n3) Editar el nombre de un grupo \n4) Borar un grupo
6) Ver que contactos estan en un grupo y agregar o sacar a otro \n7) Ver a que grupos pertenese un contacto y agregar o sacar a otro\nPrecione cualquier tecla para regresar\n""")

                    match opsion :
                        case "1" :
                            while True :
                                print (f"Grupos existentes : \n{TG.ver_contenido_Grupos ()}")
                                nuevo_contenido = input ("Nombre del nuevo grupo :\n")

                                if TG.grupo_espesifico_linia (nuevo_contenido) :
                                    print (f"El grupo {nuevo_contenido} ya existe\n")

                                else :
                                    TG.grupo_nuevo (nuevo_contenido)

                                de_donde = "crear otro grupo"
                                if regresar (de_donde) :
                                    break

                        case "2" :
                            print (f"Grupos :\nID  Nombre de los grupos\n{TG.ver_contenido_Grupos()}")

                        case "3" :
                            while True :
                                print (f"Grupos :\nID  Nombre de los grupos\n{TG.ver_contenido_Grupos()}")
                                mensaje = "Elegir el ID del nombre del grupo a editar ID : "
                                por_ID = si_nummeros (mensaje)

                                if TG.nombre_grupo_id (por_ID) is True:
                                    print (f"No existe ningun grupo con el ID {por_ID}\n")

                                else :
                                    contenido_editado = input ("Nuevo nombre :")
                                    if TG.grupo_espesifico_linia (contenido_editado) :
                                        print (TG.nombre_grupo_id (por_ID))
                                        print (f"El grupo {contenido_editado} ya existe\n")

                                    else :
                                        print (f"Seguro que quieres editar a {TG.nombre_grupo_id (por_ID)}\n1) Si \n2) No")
                                        seguro = input ()

                                        if seguro == "1" :
                                            print (f"\nCambiastes {TG.nombre_grupo_id (por_ID)}")
                                            TG.actualisar_fila_grupos (contenido_editado, por_ID)
                                            print (f"Por {TG.nombre_grupo_id (por_ID)}\n")

                                de_donde = "editar otro grupo"
                                if regresar (de_donde) :
                                    break

                        case "4" :
                            while True :
                                print(f"ID  Nombre de los grupos\n{TG.ver_contenido_Grupos ()}")
                                mensaje = "Escrive el ID del grupo a borrar\n"
                                borrar_ID = si_nummeros (mensaje)

                                if TG.nombre_grupo_id (borrar_ID) is True:
                                    print (f"No existe ningun grupo con el ID {borrar_ID}\n")

                                else :
                                    print (f"Seguro que quieres borrar a {TG.nombre_grupo_id (borrar_ID)}\n1) Si \n2) No")
                                    seguro = input ()

                                    if seguro == "1" :
                                        TG.borrar_grupo (borrar_ID) 

                                de_donde = "borrar otro grupo"
                                if regresar (de_donde) :
                                    break

                        case "6" :
                            while True :
                                print (f"\nID  Nombre de los grupos\n{TG.ver_contenido_Grupos()}")
                                mensaje = "Elegir el id del grupo a ver : "
                                grupo_id = si_nummeros (mensaje)

                                if TG.nombre_grupo_id (grupo_id) is True:
                                    print (f"No existe ningun grupo con el ID {grupo_id}\n")

                                else :
                                    print (f"En el grupo {TG.nombre_grupo_id (grupo_id)[1]} se encuentran estos contactos :")
                                    print (f"ID,Nomvre, Apellido, Telefono, Emeil\n{TR.contactos_en_grupos (grupo_id)}")

                                    print (f"1) Quieres agregarle un nuevo contacto al grupo {TG.nombre_grupo_id (grupo_id)} \n2) Queres sacarle algun contacto del grupo {TG.nombre_grupo_id (grupo_id)} \n3) Ninguna\n")
                                    quiero = input ()

                                    if quiero == "1" :
                                        print(f"Contactos \nID,Nomvre, Apellido, Telefono, Emeil\n{TC.ver_contenido_Contactos ()}")
                                        mensaje = "Escrive el ID del contacto a agregar \n"
                                        contacto_id = si_nummeros (mensaje)

                                        if TC.contacto_espesifico_id(contacto_id) is True :
                                            print (f"El ID seleccionar ({contacto_id}) no existe verifique el ID")

                                        else :
                                            print (f"Seguro que quiere agregar a {TC.contacto_espesifico_id(contacto_id)}\nal grupo {TG.nombre_grupo_id (grupo_id)[1]}\n1) Si \n2) No")
                                            seguro = input ()

                                            if seguro == "1" :
                                                if TR.relacionamiento_nuevo (contacto_id, grupo_id) is True:
                                                    print ("El contacto ya esta en ese grupo")

                                    elif quiero == "2" :
                                        mensaje = "Selecsione el ide del contacto a sacar :"
                                        contacto_id = si_nummeros (mensaje)

                                        if TR.desrelacionar_contacto_grupo(contacto_id, grupo_id) is True:
                                            print (f"No existe ningun contacto con el ID {contacto_id}\n")

                                de_donde = "ver otro grupo"
                                if regresar (de_donde) :
                                    break

                        case "7" :
                            while True :
                                print(f"Contactos \nID,Nomvre, Apellido, Telefono, Emeil\n{TC.ver_contenido_Contactos ()}")
                                mensaje = "Elegir el id del contacto a ver : "
                                contacto_id = si_nummeros (mensaje)

                                if TC.contacto_espesifico_id(contacto_id) is True :
                                    print (f"El ID seleccionar ({contacto_id}) no existe verifique el ID")

                                else :
                                    print (f"\nEste contacto {TC.contacto_espesifico_id (contacto_id)}")
                                    print (f"Esta en estos grupos :\n{TR.grupos_en_contactos (contacto_id)}")

                                quiero = input ("1) Quieres agregarle un nuevo grupo al contacto seleccionar \n2) Queres sacarle algun grupo al contacto seleccionar \n3) Ninguna\n")

                                if quiero == "1" :
                                    print (f"\nID  Nombre de los grupos\n{TG.ver_contenido_Grupos()}")

                                    mensaje = "Elegir el id del grupo a agregar : "
                                    grupo_id = si_nummeros (mensaje)

                                    if TG.nombre_grupo_id (grupo_id) is True:
                                        print (f"No existe ningun grupo con el ID {grupo_id}\n")

                                    else :
                                        print (f"Seguro que quiere agregar a {TC.contacto_espesifico_id(contacto_id)}\nal grupo {TG.nombre_grupo_id (grupo_id)[1]}\n1) Si \n2) No")
                                        seguro = input ()

                                        if seguro == "1" :
                                            if TR.relacionamiento_nuevo (contacto_id, grupo_id) is True:
                                                print ("El contacto ya esta en ese grupo")

                                elif quiero == "2" :
                                    mensaje = "Selecsione el ide del grupo a sacar :"
                                    grupo_id = si_nummeros (mensaje)

                                    if TR.desrelacionar_contacto_grupo(contacto_id, grupo_id) is True:
                                        print (f"No existe ningun grupo con el ID {grupo_id}\n")

                                de_donde = "ver otro contacto"
                                if regresar (de_donde) :
                                    break

                        case _ :
                            break

            case _ :
                print ("Adios")
                break

def regresar (de_donde) :
    opsion = input (f"Desea {de_donde} 1) Si 2) No\n")
    if opsion == "1" :
        return False
    else :
        return True

def si_nummeros (mensaje) :
    while True :
        try :
            numero = int (input (mensaje))
            return numero

        except ValueError :
            print (f"Estos caracteres {numero} no es válido")

menu ()