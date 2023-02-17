año = int (input("que año queres saber si es bisiesto "))

resultado01 = año % 4
resultado02 = año % 100
resultado03 = año % 400

def calculo () :
    if resultado01 == 0 :
        if resultado02 == 0 :
            if resultado03 == 0 :
                biciesto = True
            else:
                biciesto = False
        else:
            biciesto = True
    else:
        biciesto = False
    if biciesto == True :
        print (año," si es un año bisiesto")
    else:
        print ( año," no es un año bisiesto")

calculo ()