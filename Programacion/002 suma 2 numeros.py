def pedir_numero():
    while True:
        try:
            N1 = int(input ( "poneme el numero que quieras " ))
            break
        except ValueError:
            print("te dije que me pongas un numero ")
 

# una funcion es un bloque de codigo que hace algo  
# antes de poder usar una funcion ahi que definirla (def)
# tienen un nombre y pueden ser usadas munchas veses
# una funcion tambien puede retornar un balor 
pedir_numero()

        
while True:
    try:
        N2 = int(input ( "poneme el otro numero que quieras " ))
        break
    except ValueError:
        print("te dije que me pongas un numero ")

print (N1+N2)