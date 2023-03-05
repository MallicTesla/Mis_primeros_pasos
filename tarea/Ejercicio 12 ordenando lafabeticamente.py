paices = input ("Escrive unos cuantos nombres de paises separados por coma no importa si se repiten ")

lista = paices.split(",")
resultado_1 = sorted (set (lista))

resultado_3 = []

for resultado_2 in resultado_1 :
    resultado_3.append (resultado_2 + ",")

lista_final = "".join (resultado_3)

print ("Este seria el orden alfabetico de los paises2: \n", lista_final)

#  India, Rusia, México, Portugal, Brasil, Ecuador, Colombia, Perú, Japón, Uruguay, Uruguay, Francia, Reino Unido, España, Estados Unidos, Alemania, Venezuela, Chile, Uruguay, Canadá