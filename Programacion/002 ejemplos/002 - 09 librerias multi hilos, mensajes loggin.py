# # -----------------------------------programasion multi hilo--------------------------------------------------------------
# import _thread
# import time

# def hora_actual (nombre_thread, tiempo_de_espera) :
#     time.sleep(tiempo_de_espera)
#     print(f"hilo {nombre_thread} - {time.ctime(time.time())}")

# _thread.start_new_thread(hora_actual,("thread uno ", 1))
# _thread.start_new_thread(hora_actual,("thread dos ", 2))

# print ("ya ejecuto lo hilos")
# #   cuando se ejecuta codigo multi hilo tenemos que darle tiempo al programa para que se ejecute 
# #   esta son las formas mas faisles de hacerlo 
# # while True :
#     # pass              #   se queda el programa atscado y sobrecarga el prosesador 

# while True :
#     time.sleep(0.1)   #   se queda el programa atscado y no sobrecarga tanto a el prosesador 

# # time.sleep(0.1)         #   finalisa el programa

#-----------------------------------loggin-----------------------------------------------------------------------
# sirve para generar mensajes de registro

import logging

logging.basicConfig(level=logging.DEBUG)   #   para ver todos los mensajes desde (DEBUG) a mas severos

logging.critical (" 4) critico")
logging.error ("    3) error")
logging.warning("  2) ejecutando warning")
logging.info ("     1) arancando programa")
logging.debug ("    0) debug")