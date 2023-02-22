#   los modulos se llaman igual que el fichero
#   todo el codigo se deveria cologar dentro de una unica funcion
#   cuando se llama a un modulo se ejecuta tdo lo que esta en el por eso los modulos estan compuestos prinsipal mente por funciones y clases

import codigomodulo as C                            #   llamo al modulo

def main () :
    Rsuma = C . mas ( 2 , 2 )
    Rresta = C . menos ( 5 , 3 )
    print ("estoy en main():" , Rsuma , Rresta )

def main2 () :
    print (C.Como_me_llamo () )





if __name__ == "__main__" :
    main2 ()

