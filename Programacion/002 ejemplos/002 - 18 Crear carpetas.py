import os

ruta = "C:/Users/Mallic/Downloads"
nombre_principal = "/YouTube"
ruta_principal = ruta + nombre_principal

subcarpeta_1 = "Video"
subcarpeta_2 = "Audio"




# Verifica si la carpeta principal ya existe
if not os.path.exists(ruta_principal):
    print(f"La carpeta principal '{nombre_principal}' no existe.")
    # Crea la carpeta principal
    os.makedirs(ruta_principal)
    print(f"Carpeta principal '{nombre_principal}' creada.")
else:
    print(f"La carpeta principal '{nombre_principal}' ya existe.")

# Verifica si la subcarpeta 1 ya existe
ruta_subcarpeta_1 = os.path.join(ruta_principal, subcarpeta_1)
if not os.path.exists(ruta_subcarpeta_1):
    print(f"La subcarpeta '{subcarpeta_1}' no existe.")
    # Crea la subcarpeta 1 dentro de la carpeta principal
    os.makedirs(ruta_subcarpeta_1)
    print(f"Subcarpeta '{subcarpeta_1}' creada dentro de la carpeta principal.")
else:
    print(f"La subcarpeta '{subcarpeta_1}' ya existe dentro de la carpeta principal.")

# Verifica si la subcarpeta 2 ya existe
ruta_subcarpeta_2 = os.path.join(ruta_principal, subcarpeta_2)
if not os.path.exists(ruta_subcarpeta_2):
    print(f"La subcarpeta '{subcarpeta_2}' no existe.")
    # Crea la subcarpeta 2 dentro de la carpeta principal
    os.makedirs(ruta_subcarpeta_2)
    print(f"Subcarpeta '{subcarpeta_2}' creada dentro de la carpeta principal.")
else:
    print(f"La subcarpeta '{subcarpeta_2}' ya existe dentro de la carpeta principal.")