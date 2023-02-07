def pedir_numero(texto):
     while True:
        try:
            return int(input (texto ))
        except ValueError:
            print("te dije que me pongas un numero ")

print ("Elegi el tipo de operasion")
opsiones = ["", "+ _ a", "- _ b", "* _ c", "/ _ d " ]
for tipo in opsiones:
    print(tipo)

operasion = input ()


N1 = pedir_numero( "poneme el numero que quieras ")
N2 = pedir_numero("pone el otro numero ")

if operasion == "a":
    print (N1+N2)
    print ("elegistes + ")
elif operasion == "b":
    print (N1-N2)
    print("elegistes - ")
elif operasion == "c":
    print (N1*N2)
    print ("elegistes * ")
elif operasion == "d":
    print (N1/N2)
    print ("elegistes / ")
else:
    print("mira que solo podes elegir a,b,c,d")
    