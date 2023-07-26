#   en este patron de diseño las clases pueden tener una sola instansia y un punto de acseso a esa instansia

#   asi es como se ase en jaba tradusido a python

# #   object es la clase padre
# class Usuario (object):
#     __instanse = None

#     #   como __new__ es un metodo estatico se usa cls que hace referensia a la clase
#     def __new__(cls) :
#         if Usuario.__instanse is None:
#             print ("nueva instancia")
#             Usuario.__instanse = object.__new__(cls)

#         return Usuario.__instanse



# if __name__ == "__main__" :
#     usuario_1 = Usuario ()
#     usuario_2 = Usuario ()

#     print (usuario_1 is usuario_2)

#--------------------------------------------------------------------------------------------------------------------
#   asi se hace atraves de decorados

#   esto es un decorador el decorador se puede usar en todas las clases
def singleton (cls):
    instansias = dict()

    #   *args(listado de argumentos) **kwargs (dicsionario de argumentos)
    def wrap (*args, **kwargs):
        #   cls que hace referensia a la clase
        #   si la clase a decorar (cls) no se encuentra dentro del dicsionario (instansias) se agrega junto con su corespondiente instansia (cls(*args, **kwargs))
        #   despues retorna el objeto
        if cls not in instansias :
            instansias[cls] = cls(*args, **kwargs)

        return instansias[cls]

    return wrap

@ singleton
class Usuario (object):
    def __init__(self, username):
        self.username = username

@ singleton
class Admin ():
    pass



if __name__ == "__main__" :
    usuario_1 = Usuario ("Pablo")
    usuario_2 = Usuario ("Mallic")

    admin_1 = Admin ()
    admin_1 = Admin ()

    print (usuario_1 is usuario_2)
    print (admin_1 is admin_1)
