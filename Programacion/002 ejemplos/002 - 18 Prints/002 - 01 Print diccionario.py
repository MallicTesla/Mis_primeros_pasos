diccionario = {'1': 1, '2': 0, '3': 0, '4': 0, '5': 1, '6': 0, '7': 0, '8': 0, '9': 1}

if diccionario.get('5') == 1 and diccionario.get('1') == 1 and diccionario.get('9') == 1:
    print(True)
else:
    print(False)

diccionario1 = { "Thriller": "1982", "Back in Black": "1980", "The Dark Side of the Moon": "1973", "The Bodyguard": "1992",
                "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", "Saturday Night Fever": "1977", "Rumours": "1977"}

print ( 1, diccionario1.keys())                      # asi optenes solo el valor de todas las llaves
print ( 2, diccionario1.values())                    # asi optenes el valor de todos los valores
print ( 3, "Back in Black" in diccionario1)          # rebisa si esa key se encuentra dentro del diccionario

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
intersection = album_set1 & album_set2              # asi comparas dos set para ver los valores en comun

print ( 4,intersection)
print ( 5, album_set1.difference(album_set2))       # muestra las diferensias de la lista album_set1 con respecto de la lista album_set2
print ( 6, album_set1.union(album_set2))            # une las dos listas sin que se repitan los valores

print ( 7, set({"Back in Black", "AC/DC"}).issubset(album_set1))    #comprueva si un conjunto/set esta dentro de otro


x=1
x>-5

print (x)
