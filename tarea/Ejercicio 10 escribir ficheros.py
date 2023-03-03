f = open ("C:\Pruevas\ejercicio10.txt", "w")

f.write("espero\n")
f.write("que\n")
f.write("sea\n")
f.write("esto")

f.close()

print ("fin de escritura y comienso de lectura")

f = open ("C:\Pruevas\ejercicio10.txt", "r") 

datos = f.read()

f.close()

print (datos)