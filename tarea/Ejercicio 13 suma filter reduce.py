numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado1 = filter(lambda x : x % 2 != 0, numero) 

from functools import reduce

resultado2 = reduce (lambda a , b : a + b , resultado1)

print (resultado2)