from datetime import datetime

class Tiempo:
    def __init__(self):
        now = datetime.now()
        self.añoo = now.year
        self.mess = now.month
        self.semanaa = now.weekday()
        self.diaa = now.day
        self.horaa = now.hour
        self.minutoss = now.minute
        self.segundoss = now.second

class Fecha_actual(Tiempo):
    def __init__(self):
        super().__init__()
        self.meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        self.dias = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "sabado", "Domingo")
        self.mes = self.meses[self.mess - 1]

    def __str__(self):
        return "Hoy es {} {} de {} del {}".format(self.dias[self.semanaa], self.diaa, self.mes, self.añoo)

class Hora_actual (Tiempo) :
    def __str__(self):
        super().__init__()
        return "Son las {:02d}:{:02d}:{:02d}". format (self.horaa, self.minutoss, self.segundoss) 

class Tiempo_restante(Tiempo):
    def calculo_horas (self):
        tiempo = self.hora_deseada - datetime.now()
        horas = tiempo.seconds // 3600
        minutos = (tiempo.seconds // 60) % 60
        segundos = tiempo.seconds % 60
        return "{:02d}:{:02d}:{:02d}".format(horas, minutos, segundos)
    
class Alarma(Tiempo_restante):
    def __init__(self, hora, minuto, segundo):
        super().__init__()
        self.hora_deseada = datetime.now().replace(hour=hora, minute=minuto, second=segundo)

class Salida(Alarma):
    def __init__(self, hora, minuto, segundo):
        super().__init__(hora, minuto, segundo)

    def __str__(self):
        tiempo_restante = self.calculo_horas()
        return "Te quedan {} de trabajo, salis a las {}".format(tiempo_restante, self.hora_deseada.strftime("%H:%M:%S"))

class Entrada(Alarma):
    def __init__(self, hora, minuto, segundo):
        super().__init__(hora, minuto, segundo)

    def __str__(self):
        tiempo_restante = self.calculo_horas()
        return "En {} entras al trabajo, entras a las {}".format(tiempo_restante, self.hora_deseada.strftime("%H:%M:%S"))

class Programacion (Tiempo) :
    def __str__(self):
        self.dias = [self.semanaa]
        self.valor = self.dias [0]

        if self.valor <= 4:                         #   ultimo dia laboral de la semana va del 0 al 6 lunes es 0 y domingo es 6
            if self.horaa <= 17:                    #   hora de slaida
                if self.horaa >= 10:                #   hora de entrada
                    return str(salida)
                else:
                    return str(enrada)
            elif self.valor >= 4 :                  #   ultimo dia laboral de la semana va del 0 al 6 lunes es 0 y domingo es 6
                if self.horaa >= 17:                #   hora de salida
                    return "Ofisialmente ya comenso el fin de semana"
            else:
                return str(enrada)
        else:
            return "Es fin de semanaaaaaa"

fecha = Fecha_actual ()
hora = Hora_actual ()
salida = Salida (17, 00, 00)                        #   coloca tu hora de salida del trabajo: hora, minutos, segundos
enrada = Entrada (10, 00, 00)                       #   coloca tu hora de entrada al trabajo: hora, minutos, segundos
P = Programacion ()

print (fecha)
print (hora)
print (P)

#   para llamar un metodo __str__ se usa str()
#   para retornar un __str__ de una clase ya instansiada dentro de otra clase instanciada se usa (return str()) y despues el print