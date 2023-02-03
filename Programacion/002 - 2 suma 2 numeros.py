# una funcion es un bloque de codigo que hace algo  
# antes de poder usar una funcion ahi que definirla (def)
# tienen un nombre y pueden ser usadas munchas veses
# una funcion tambien puede retornar un balor 


def pedir_numero(texto):
     while True:
        try:
            return int(input (texto ))
        except ValueError:
            print("te dije que me pongas un numero ")

N1 = pedir_numero( "poneme el numero que quieras ")
N2 = pedir_numero("pone el otro numero ")        
print (N1+N2)