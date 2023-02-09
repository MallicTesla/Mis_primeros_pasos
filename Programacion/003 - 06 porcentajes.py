def pedir_numero(texto):
        while True:
            try:
                return int(input (texto ))
            except ValueError:
                print("te dije que me pongas un numero ")
def porcentaje () :
    print("que estas buscando")
    quiero = ["pone 1 calcular el total conociendo un porcentaje.", "pone 2 calcular el porcentaje de una cantidad dada", "pone 3 calcular qué porcentaje del total es una cantidad" ]
    for queres in quiero:
        print(queres)

    quiero = input ()

    if quiero == "1":
        N3 = pedir_numero ("valor del porcentaje ")
        N4 = pedir_numero ("el porcentaje ")
        R1 = (N3*100/N4)
        print("si" ,N4, "porciento es" ,N3, "entonses el cien pociento es" ,R1, )
    elif quiero == "2":
        N4 = pedir_numero ("el porcentaje ")
        N5 = pedir_numero ("pone el valor del cien porciento ")
        R1 = (N4*N5/100)
        print ("el" ,N4, "porciento de" ,N5, "es" ,R1,)
    elif quiero == "3":
        N3 = pedir_numero ("valor del porcentaje ")
        N5 = pedir_numero ("pone el valor del cien porciento ")
        R1 = (N3*100/N5)
        print("si" ,N5, "es el cien porciento entonses" ,N3,"es el",R1, "porciento")
    else:
        print("mira que solo podes elegir entre 1-2-3")
        return porcentaje ()
porcentaje ()
    #N3 = pedir_numero ("valor del porcentaje ")
    #N4 = pedir_numero ("el porcentaje ")
    #N5 = pedir_numero ("pone el valor del cien porciento ")

    