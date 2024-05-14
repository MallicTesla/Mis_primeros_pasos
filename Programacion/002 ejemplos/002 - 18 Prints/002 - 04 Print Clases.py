class Persona:
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona = Persona ("Juan", 30)

# La función getattr en Python se utiliza para obtener el valor de un atributo de un objeto de manera dinámica. Es especialmente útil cuando el nombre del atributo no es
#   conocido hasta el tiempo de ejecución.

# getattr(obj, attr_name, default)
# obj           es el objeto del cual quieres obtener el atributo.
# attr_name     es una cadena que representa el nombre del atributo que deseas obtener.
# default       es un valor opcional que se devolverá si el atributo no existe en el objeto. Si no se proporciona y el atributo no se encuentra, se lanzará una excepción
#                   AttributeError.

# Obtener el valor del atributo 'nombre'
nombre = getattr (persona, 'nombre')
print (nombre)  # Salida: Juan

# Obtener el valor del atributo 'edad'
edad = getattr (persona, 'edad')
print (edad)  # Salida: 30

# Intentar obtener un atributo inexistente sin valor por defecto
# Esto lanzará una excepción AttributeError
# direccion = getattr(persona, 'direccion')

# Intentar obtener un atributo inexistente con valor por defecto
direccion = getattr (persona, 'direccion', 'No disponible')
print (direccion)  # Salida: No disponible
