def calculo ():
    def pedir_numero(texto):
        while True:
            try:
                return int(input (texto ))
            except ValueError:
                print("te dije que me pongas un numero ")

    esta = True
    while esta:
        print ("Elegi el tipo de operasion")
        opsiones = ["", "+", "-", "*", "/ " ]
        for tipo in opsiones:
            print(tipo)

        operasion = input ()
        
        N1 = pedir_numero( "poneme el numero que quieras ")
        N2 = pedir_numero("pone el otro numero ")


        if operasion == "+":
            print ("elegistes + ")
            print (N1+N2)
            p = input ("queres realisar otra operasion si / no ")
            if p == "si":
                calculo ()
            else:
                print("nos vemos ")
                esta = False
        elif operasion == "-":
            print("elegistes - ")
            print (N1-N2)
            p = input ("queres realisar otra operasion si / no ")
            if p == "si":
                calculo ()
            else:
                print("nos vemos ")
                esta = False
        elif operasion == "*":
            print ("elegistes * ")
            print (N1*N2)
            p = input ("queres realisar otra operasion si / no ")
            if p == "si":
                calculo ()
            else:
                print("nos vemos ")
                esta = False
        elif operasion == "/":
            print ("elegistes / ")
            print (N1/N2)
            p = input ("queres realisar otra operasion si / no ")
            if p == "si":
                calculo ()
            else:
                print("nos vemos ")
                esta = False
        else:
            print("mira que solo podes elegir +,-,*,/")
calculo()