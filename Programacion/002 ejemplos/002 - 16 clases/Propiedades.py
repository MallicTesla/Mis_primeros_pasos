class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario

# #   asi se opstiene el valor del atrivuto
#     def getnombre (self):
#         return self.__nombre

#     def getsalario (self):
#         return self.__salario

#     #   asi es para modificar un atributo encapsulado
#     def setnombre (self, nombre):
#         self.__nombre = nombre

#     def setsalario (self, salario):
#         self.__salario = salario

#     #   asi es para borrar un atrivuto encapsulado
#     def delnombre (self):
#         del self.__nombre

#     def delsalario (self):
#         del self.__salario

# -----------con property-----------------------

#   asi se opstiene el valor del atrivuto
    def __getnombre (self):
        return self.__nombre

    def __getsalario (self):
        return self.__salario

    #   asi es para modificar un atributo encapsulado
    def __setnombre (self, nombre):
        self.__nombre = nombre

    def __setsalario (self, salario):
        self.__salario = salario

    #   asi es para borrar un atrivuto encapsulado
    def __delnombre (self):
        del self.__nombre

    def __delsalario (self):
        del self.__salario

    nombre = property ( fget = __getnombre,
                        fset = __setnombre,
                        fdel = __delnombre,
                        doc = "soy la propiedad del 'nombre'")

    salario = property (fget = __getsalario,
                        fset = __setsalario,
                        fdel = __delsalario,
                        doc = "soy la propiedad del 'salario'")


# asi se hace sin encapsular los modelos

# #   asi lo creo
# empleado_1 = Empleado("Mallic", 23130)
# print (f"{empleado_1.getnombre()} tiene un salario de {empleado_1.getsalario()}")

# #   y asi lo edito
# empleado_1.setnombre ("German")
# print (f"{empleado_1.getnombre()} tiene un salario de {empleado_1.getsalario()}")

# #   y esto es lo boraria
# # empleado_1.delnombre ()
# # print (f"{empleado_1.getnombre()} tiene un salario de {empleado_1.getsalario()}")

# -----------con property-----------------------

#   asi lo creo
empleado_1 = Empleado("Mallic", 23130)
print (f"{empleado_1.nombre} tiene un salario de {empleado_1.salario}")

#   y asi lo edito
empleado_1.nombre = "German"
print (f"{empleado_1.nombre} tiene un salario de {empleado_1.salario}")
