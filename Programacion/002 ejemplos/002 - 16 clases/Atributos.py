class Persona () :
    edad = 27
    nombre = "Mallic"
    pais = "brazil"

doctor = Persona ()

print ("La edad es", doctor.edad)
#   asi se acsede al atrivuto directamente
print ("La edad es", getattr(doctor, "edad"))

#   asi averiguas si existe un atributo devuelve un buliano
print ("El doctor tiene una edad", hasattr(doctor,"edad"))
print ("El doctor tiene una edad", hasattr(doctor,"alellido"))

print ("antes", doctor.nombre)
#   asi se le cambia el valor a un atributo
#   primero se llama al objeeto sespues se coloca el atributo y despues por lo que lo queres cambiar
setattr (doctor,"nombre", "Tesla")
print ("ahora", doctor.nombre)

print ("antes el doctor es de ", hasattr(doctor,"pais"))
#   para borar un atributo
#   se coloca la clase y el atributo
delattr (Persona, "pais")
print ("despues el doctor es de ", hasattr(doctor,"pais"))


