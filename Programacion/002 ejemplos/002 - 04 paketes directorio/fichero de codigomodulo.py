#   los modulos se llaman igual que el fichero
#   todo el codigo se deveria cologar dentro de una unica funcion
#   cuando se llama a un modulo se ejecuta todo lo que esta en el por eso los modulos estan compuestos prinsipal mente por funciones y clases
#   cuando se crea un directorio se llama ala carpeta (directorio) y luego al modulo
#   tiene que tener un fichero espesial llamado (__init__.py)

from directorio import codigomodulo as D0                            #   llamo al modulo
#import directorio.codigomodulo as D                                #   otra forma de hacer lo mismo

from directorio.otrodirectorio1 import codigomodulo1 as D1
from directorio.otrodirectorio1 import codigomodulo1 as D2

def D_0 () :
    Rsuma = D0 . mas ( 2 , 2 )
    Rresta = D0 . menos ( 5 , 3 )
    print ("estoy en main():" , Rsuma , Rresta )
    print ("resultado de ",D0.Como_me_llamo () )

def D_1 () :
    Rsuma = D1 . mas ( 2 , 2 )
    print ("estoy en main():" , Rsuma )
    print ("resultado de ",D1.Como_me_llamo () )

def D_2 () :
    Rresta = D2 . menos ( 5 , 3 )
    print ("estoy en main():" , Rresta )
    print ("resultado de ",D2.Como_me_llamo () )

def main2 () :
    print (D0.Como_me_llamo () )
    print (D1.Como_me_llamo () )
    print (D2.Como_me_llamo () )





D_0 ()
D_1 ()
D_2 ()
