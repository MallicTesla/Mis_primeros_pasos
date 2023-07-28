# class Persona () :
#     #   __init es un constructor que ese ejecuta cuando llamas al objeto
#     def __init__ (self, nombre, año) :
#         self.nombre = nombre
#         self.año = año

#     def descipcion (self) :
#         return f"{self.nombre} tiene { self.año} años"

#     def comentario (self, frase) :
#         return f"{self.nombre} dise {frase}"

# doctor = Persona("Mallic", 25)
# print (doctor.descipcion())

# print (doctor.comentario ("ola k ase"))


# -------------------------------------

class Emeil () :
    def __init__ (self):
        self.enviado = False

    def enviar_coreo (self):
        self.enviado = True

mi_correo = Emeil()
print (mi_correo.enviado)

mi_correo.enviar_coreo ()
print (mi_correo.enviado)



