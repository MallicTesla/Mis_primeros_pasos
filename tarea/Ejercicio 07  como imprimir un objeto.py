class Alumno () :
        
    def __init__ (self, nombre, nota) :
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        if self.nota >= 6 :
            return "EL alumno {} aprobado con {} " .format (self.nombre,self.nota)
        else :
            return "EL alumno {} reprobo con {} " .format (self.nombre,self.nota)

A = Alumno ("Manolo",6)
print(A)