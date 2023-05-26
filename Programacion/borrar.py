import re

texto = "54_564/cua.5tro/menu_crear/emple_ado/"

match = re.search(r"/(\w+)/", texto)
if match:
    palabra_buscada = match.group(1)
    print(palabra_buscada)