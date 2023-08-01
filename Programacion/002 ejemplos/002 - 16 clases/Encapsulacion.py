class Cliente:
    def __init__(self) :
        #   para encapsularlo se agrega doble bara vaja __ seguido del nombre de la variavle
        #   asi no se muestr el valor
        self.__codigo = 1234

    #   los metodosse encapsulan de a misma forma
    def __cuenta (self):
        print("cuenta")

    #   con esta funsion mostras el valor del atrivuto encapsulado
    #   al prinsipio va get seguido del nombre del atributo todo junto
    def getcodigo (self):
        return self.__codigo

persona = Cliente()
#   para mostrar el valor de un atrivuto encapsulado se ase asi
#   objeo._nombreclase__atributo
print (persona._Cliente__codigo)

#   para mostrar un metodo encapsulado se hace asi sin pasos previos
#  objeto._nombreclase__metodo()
persona._Cliente__cuenta()


