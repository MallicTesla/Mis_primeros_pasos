# # ------------------------------------------------filter--------------------------------------

# numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def mifuncion (x) :
#     if x % 2 == 0 :
#         return True

# #   filter revisa la funcion pasando el parametro (mifuncion, numero) y ve si devuelve True o False y elimina el elemento que da false
# #   devuelve una lista
# resultado1 = filter(mifuncion, numero) 
# #   tambien se puede hacer con una lambda
# resultado2 = filter(lambda x : x % 2 == 0, numero) 

# print (list (resultado1))
# print (list (resultado2))

# # -------------------------------------------map----------------------------------------------------

def cuadrado (x):
    return x * x

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#   map aplica la funcion en cada elemento de la lista
resultado1 = map (cuadrado,numero )
#   tambien se puede hacer con una lambda
resultado2 = map (lambda x : x * x , numero)

print (list (resultado1))
print (list (resultado2))

# # -------------------------------------reduce-------------------------------------------------------
# from functools import reduce

# def suma (a, b) :
#     print (f"a={a} b={b}")
#     return a + b

# numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# #   reduce aplica la funcion a una lista hasta que queda un solo elemento
# #   la funcion nesesita 2 parametros que puede ser el mismo parametro
# resultado1 = reduce(suma,numero)
# #   tambien se puede hacer con una lambda
# resultado2 = reduce (lambda a , b : a + b , numero)

# print (resultado1)
# print (resultado2)

# # ----------------------------------------zip-------------------------------------------------------

# cursos = ["java ","python ", "git "]
# numero_clases = [5,15,2]
# alumnos = [2,30,32,5]

# #   junta elementos que esta en la misma posision de cada lista y entrega un dicsionario
# #   solo junta elemnentos y devuelve la misma cantidad que la lista mas pequeña
# resultado1 = zip (cursos,numero_clases,alumnos)

# print (list (resultado1))

# # -----------------------------------any()--all()---------------------------------------------------

# #   se usan para verificar que todas o una condision de una lista se cumpla

# lista1 = [ 1== 1 , 2 == 2 , 3 == 4]

# resultado1 = any (lista1)       #   si un elemento de la lista es verdadero debuelve True

# resultado2 = all (lista1)       #   si todos los elementos de la lista son verdaderoos devuelve True

# print (resultado1)
# print (resultado2)

# # ------------------------------------round--------------------------------------------------------------
# #   redondea al numero mas sercana

# a = 5.4
# b = 5.5
# c = 5.6

# print(round(a))
# print(round(b))
# print(round(c))

# ---------------------------------------------------------------------------------------------------------
# #   devuelve el elemento mas vajo
# print (min(5,3,6,8,7,1))
# #   devuelve el elemento mas alto
# print (max(5,3,6,8,7,1))

# #   eleva el primer numero por el segundo
# print (pow(2,5))
# # es lo mismo 
# print (2**5)

# # ordenar una lidta alfaveticamente 
# lista = ["z","o","a","b","j","s","c","g",]
# ordenada1 = sorted (lista)
# #   asi se ordena alreves
# ordenada2 = sorted (lista, reverse=True)

# print (ordenada1)
# print (ordenada2)