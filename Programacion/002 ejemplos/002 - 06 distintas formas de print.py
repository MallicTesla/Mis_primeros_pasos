numero = 15
texto = "ola ke ase"
otro_mas = 1.

#   esta es la forma vieja
#   %d = digito, %s = strint % = flotante 
# print ("el numero es %d y el texto es %s y otromas %.2f" % (numero, texto, otro_mas)) # en caso de numeros flotantes se puede agregar un punto y despues la cantidad de dijitos despues del punto

# -------------------------------------------------------------
# #   la forma intermedia
# print ("el numero es {} y el texto es {} y otromas {}"
#         .format (numero, texto, otro_mas))
# #   otra forma de hacerlo no muy prlolija
# print ("el numero es {1} y el texto es {0} y otromas {2}" # si se colocan numeros dentro ({1}) hace referansia a la posision de los elementos en .format
#         .format (texto, numero, otro_mas))
# #   otra forma de hacer lo mismo pero mas prolijo
# print ("el numero es {num} y el texto es {tex} y otromas {om}" .format (tex = texto, num = numero, om = otro_mas))

# -------------------------------------------------------------
#   otra forma mas nueva y mas avitual de hacerlo
#   tambien es mas comun crear una variable con el texto y luego el print
# imprimir = f"el numero es {numero} y el texto es {texto} y otromas {otro_mas}"
# print (imprimir)
# #   en este caso las variables se tratan como codigo python
# def claculo (a,b):
#     return a + b
# print (f"el numero es {claculo(numero,numero)} y el texto es {texto.upper()} y otromas {otro_mas}")

# -------------------------------------------------------------
cadena =  "Michael Jackson"
n_cadena ="0123456789ABCDEF"
# El primer valor antes de los dos puntos (::) representa el índice de inicio. En este caso, no se proporciona, por lo que se toma el valor predeterminado, que es 0 (el primer
#   carácter de la cadena).
# El segundo valor después de los dos puntos (::) representa el índice de finalización. En este caso, no se proporciona, por lo que se toma el valor predeterminado, que es la
#   longitud total de la cadena.
# El tercer valor después del segundo dos puntos (::) representa el paso o el incremento. En este caso, se especifica como 2, lo que significa que se seleccionan cada segundo
#   carácter de la cadena.
print ( 1 ,cadena[::2])

# toma los 5 primeros caracteres
print ( 2 ,cadena[:5:2])
print ( 3 ,n_cadena[::2])

print ( 4 ,len (cadena))                            # cuenta la cantidad de caracteres empesando del 0

print ( 5, "Michael Jackson")
print ( 6, "Michael \t Jackson")                    # agrega una tabulacion
print ( 7, "Michael \\\ Jackson")                   # con 1 sola \ aparese 1\ y con 3\\\ aparesen 2 \\
print ( 8, r"Michael \n Jackson")                   # la cadena se toma como una cadena cruda inprime literalmente lo que dice
print ( 9, cadena.upper())

print (10, cadena.replace("Michael", "Pablo"))      # remplasa la primera primera palabra por la segunda que se encuentra en los parentesis
print (11, cadena.find("Jackson"))                  # indica en que puto de la cadena comiemiensa lo que esta entre ()
# print (12, cadena.len)

print (type(int(12.3)))
type(int(12.3))








