año = int (input("que año queres saber si es bisiesto "))

resultado01 = año % 4
resultado02 = año % 100
resultado03 = año % 400

if resultado01 == 0 :
    print("paso 1 va al paso 2")
    
    if resultado02 == 0 :
        print ("paso 2 va al paso 3")
        
        if resultado03 == 0 :
            print ("paso 3 va al paso 4")
        else:
            print("paso 3 va al paso 5")
    else:
        print("paso 2 va al paso 4")
else:
    print ("paso1 va al paso 5")

