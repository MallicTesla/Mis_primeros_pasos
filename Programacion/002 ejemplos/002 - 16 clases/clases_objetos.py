class Auto :
    #   atributos
    marca = ""
    modelo = 2004
    placa = ""

#   objeto
taxi = Auto ()

print (taxi.modelo)

# -------------------------------------------------------------------

class  Nombre ():
    pass

victor = Nombre ()
maria = Nombre ()

#   si se agregan atributos fuera de la clase
victor.edad = 30
victor.sexo = "macho"
victor.pais = "uruguay"

maria.edad = 25
maria.sexo = "embra"
maria.pais = "argentian"

print (victor.edad)

print (maria.edad)



