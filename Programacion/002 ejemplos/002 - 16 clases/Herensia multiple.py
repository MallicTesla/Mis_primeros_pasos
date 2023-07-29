class Telefono:
    def __init__(self) :
        pass

    def llamar (self):
        print ("llamando")

    def ocupado (self):
        print ("ocupado")

class Camara :
    def __init__(self) :
        pass

    def fotograia (self):
        print ("tomando foto")

class Reproduccion :
    def __init__(self):
        pass

    def rep_musica (self):
        print ("reproduciendo musica")

    def rep_video (self):
        print ("reproduciendo video")

class Smartphon (Telefono, Camara, Reproduccion):
    #   Este método es un método destructor en Python, también conocido como "destructor de objetos", 
    #   osea despues de que se usa el objeto creado con esta clase se bora de la memoria
    #   El intérprete de Python se encarga de liberar la memoria de los objetos que ya no son utilizados automáticamente. 
    def __del__(self):
        print ("Telefono apagado")

celular = Smartphon()
# print (dir(celular))

celular.fotograia()
celular.llamar()


