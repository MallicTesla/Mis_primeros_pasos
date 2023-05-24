diccionario = {'1': 1, '2': 0, '3': 0, '4': 0, '5': 1, '6': 0, '7': 0, '8': 0, '9': 1}

if diccionario.get('5') == 1 and diccionario.get('1') == 1 and diccionario.get('9') == 1:
    print(True)
else:
    print(False)