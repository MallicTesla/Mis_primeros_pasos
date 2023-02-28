import datetime

hora_actual = datetime.datetime.now().time()

def alarma(hora_deseada, hora_actual):
    if hora_deseada > hora_actual:
        diferencia = datetime.datetime.combine(datetime.date.today(), hora_deseada) - datetime.datetime.combine(datetime.date.today(), hora_actual)
    else:
        diferencia = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=1), hora_deseada) - datetime.datetime.combine(datetime.date.today(), hora_actual)
    hora = diferencia.seconds // 3600
    minutos = (diferencia.seconds // 60) % 60
    return hora,minutos

hora_salida = datetime.datetime.now().replace(hour = 18, minute = 0, second = 0).time()
hora_entrada = datetime.datetime.now().replace(hour = 7, minute = 0, second = 0).time()

print(f"Son las {hora_actual.strftime('%H:%M')}")

if hora_actual >= hora_entrada :
    if hora_actual <= hora_salida :
        hora_deseada = hora_salida
        hora, minutos = alarma(hora_deseada, hora_actual)
        print ("si1")
        print(f"Te quedan {hora} horas y {minutos} minutos paras salir del trabajo salis a las {hora_deseada.strftime('%H:%M')}")
    else:
        hora_deseada = hora_entrada
        hora, minutos = alarma(hora_deseada, hora_actual)
        print ("si2")
        print(f"Dentro de {hora} horas y {minutos} minutos tenes que ir a trabajar, entras a las {hora_deseada.strftime('%H:%M')}")

else:
    hora_deseada = hora_entrada
    (hora, minutos) = alarma(hora_deseada, hora_actual)
    print ("si3")
    print(f"Dentro de {hora} horas y {minutos} minutos tenes que ir a trabajar, entras a las {hora_deseada.strftime('%H:%M')}")