def calcular ():
    ingresos = True
    gastos = True
    contador = 0
    otro1 = "s"
    otro2 = "s"

    ingreso_input = []
    gasto_input = []

    while ingresos :
        print ("\nprimero----", ingreso_input)

        if otro1.lower() == "s" :
            contador = contador + 1

            ingreso1 = int (input (f"ingreso ({contador}) " ))
            ingreso_input.append(ingreso1)
            print (ingreso_input)
            otro1 = input("otro ingreso S / N ")

            if otro1.lower() != "s" :
                ingresos = False
                resultado_ingreso = 0

                for ingreso in ingreso_input :
                    print ("por aca")
                    resultado_ingreso += ingreso

    contador = 0

    print ("\nvucle gastos")
    while (gastos):
        print ("\nprimero----", gasto_input)

        if (otro2.lower() == "s"):
            contador = contador + 1

            gasto1 = int (input (f"gasto ({contador}) " ))
            gasto_input.append(gasto1)
            print (gasto_input)
            otro2 = input("otro gasto S / N ")

            if (otro2.lower() != "s"):
                gastos = False
                resultado_gastos = 0

                for gasto in gasto_input :
                    print ("por aca")
                    resultado_gastos += gasto

    print ("\nresultado_ingreso", resultado_ingreso)
    print (  "resultado_gastos", resultado_gastos)

    return resultado_ingreso - resultado_gastos


print ("calculo",calcular ())