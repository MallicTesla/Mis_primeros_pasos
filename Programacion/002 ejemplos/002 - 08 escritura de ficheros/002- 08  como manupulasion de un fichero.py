#   open ("fichero","permiso o modo") 
#   modos: se pueden colocar mas de un modo es raro pero se puede ("rt")
#   con el caracter mas + se agrega mas funsiones como "wt+" escrive y lee en t (texto)
#   ("r" lectura)       solo lee 
#   ("a"adjuntar)       escribe en el fichero al final
#   ("w"escritura)      elimina el contenido del fichero y escrive datos sobre el
#   ("x"creacion)       se crea un fichero si no existe (en python es automatico)
#   (si se agrega"+")   
#   ("t"texto) 
#   ("b"binario)

f = open ("C:\Pruevas\hola.txt", "r")    #   para abrir un fichero  #   f es como si fuuera una instansia

# datos = f.read(10)              #   rade lee todo el fichero, si dentro de los parentesis ahi un numero es la cantidad de caracteres que muestra (cuenta los saltos de liña) 

# datos = f.readline()            #   lee la primera linia
# datos = f.readline()            #   y si se repite X cantidad de veses lee la linia X

# datos = None
# while datos != "":
#     datos = f.readline()            #     lee linia por linia 
#     print (datos)

#   lo mismo

# datos = "a"
# while len (datos) > 0:
#     datos = f.readline()
#     print (datos)

datos = f.readlines()           #   lee el fichero y lo entrega cada linia como un diccionario






f.close()                       #   para cerrar la apertura del fichero
print (datos)