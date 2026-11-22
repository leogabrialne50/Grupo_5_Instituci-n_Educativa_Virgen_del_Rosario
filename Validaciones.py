from datetime import datetime


# 1. Validar que el campo no este vacio
def validar_no_vacio(texto, nombre_campo):
    # strip() quita los espacios de los lados, asi "   " tambien cuenta como vacio
    if texto.strip() == "":
        return False, "El campo " + nombre_campo + " no puede estar vacio."
    return True, ""