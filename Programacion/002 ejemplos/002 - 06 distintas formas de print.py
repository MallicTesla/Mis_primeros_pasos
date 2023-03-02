numero = 15
texto = "ola ke ase"
otro_mas = 1.

#   esta es la forma vieja
#   %d = digito, %s = strint % = flotante 
# print ("el numero es %d y el texto es %s y otromas %.2f" % (numero, texto, otro_mas)) # en caso de numeros flotantes se puede agregar un punto y despues la cantidad de dijitos despues del punto

# #   la forma intermedia
# print ("el numero es {} y el texto es {} y otromas {}"
#         .format (numero, texto, otro_mas))
# #   otra forma de hacerlo no muy prlolija
# print ("el numero es {1} y el texto es {0} y otromas {2}" # si se colocan numeros dentro ({1}) hace referansia a la posision de los elementos en .format
#         .format (texto, numero, otro_mas))
# #   otra forma de hacer lo mismo pero mas prolijo
# print ("el numero es {num} y el texto es {tex} y otromas {om}" .format (tex = texto, num = numero, om = otro_mas))

#   otra forma mas nueva y mas avitual de hacerlo
#   tambien es mas comun crear una variable con el texto y luego el print
imprimir = f"el numero es {numero} y el texto es {texto} y otromas {otro_mas}"
print (imprimir)
#   en este caso las variables se tratan como codigo python
def claculo (a,b):
    return a + b
print (f"el numero es {claculo(numero,numero)} y el texto es {texto.upper()} y otromas {otro_mas}")








