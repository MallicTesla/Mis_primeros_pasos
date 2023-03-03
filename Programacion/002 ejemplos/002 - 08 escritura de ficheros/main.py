def main ():
    usuarios = ListarUsuarios()
    print(usuarios)
    
    for usuario in usuarios :               #   hace una lista con el return (resultados)
        print (f"usuarios {usuario}")

def ListarUsuarios ():
    f = open ("C:\Pruevas\hola.txt", "r")
    datos = f.readlines()                   #   lee el fichero y lo entrega cada linia como un diccionario
    f.close()

    resultado = []                          #   lista vasia

    for linia in datos:                     #   tranforma el disionario en una lista (linia por linia)
        if linia [0] == "#" :
            continue

        if linia [0] == "-" :
            continue

        partes = linia.split(":")           #   separa a cada linia en una lista por el parametro (:)

        print (partes[0])                   #   imprime solo el elemento X de la lista [X] empiesa en 0
        print (linia)                       #   imprime cada linia como una lista

        resultado.append(partes[0])         #   a rresultado se le agrega (partes[0])

    return resultado


if __name__ == "__main__" :
    main()