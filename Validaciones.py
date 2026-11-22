from datetime import datetime



def validar_no_vacio(texto, nombre_campo):
    
    if texto.strip() == "":
        return False, "El campo " + nombre_campo + " no puede estar vacio."
    return True, ""


def validar_dni(dni):
    dni = dni.strip()
    if dni == "":
        return False, "El DNI no puede estar vacio."
    
    if not dni.isdigit():
        return False, "El DNI solo debe tener numeros."
    if len(dni) != 8:
        return False, "El DNI debe tener exactamente 8 digitos."
    return True, ""

def validar_solo_numeros(texto, nombre_campo):
    texto = texto.strip()
    if texto == "":
        return False, "El campo " + nombre_campo + " no puede estar vacio."
    if not texto.isdigit():
        return False, "El campo " + nombre_campo + " solo acepta numeros."
    return True, ""


def validar_fecha_nacimiento(fecha):
    fecha = fecha.strip()
    if fecha == "":
        return False, "La fecha de nacimiento no puede estar vacia."

  
    try:
        fecha_convertida = datetime.strptime(fecha, "%d/%m/%Y")
    except ValueError:
        return False, "Fecha invalida. Usa el formato DD/MM/AAAA (ejemplo: 15/03/2010)."

    hoy = datetime.now()

   
    if fecha_convertida > hoy:
        return False, "La fecha de nacimiento no puede ser futura."

    
    edad = hoy.year - fecha_convertida.year
    if edad < 3 or edad > 25:
        return False, "La edad debe estar entre 3 y 25 anios para un estudiante."

    return True, ""


def validar_nota(nota):
    nota = nota.strip()
    if nota == "":
        return False, "La nota no puede estar vacia."

    
    try:
        valor = float(nota)
    except ValueError:
        return False, "La nota debe ser un numero."

    if valor < 0 or valor > 20:
        return False, "La nota debe estar entre 0 y 20."
    return True, ""


# 6. Validar el telefono del apoderado
# En Peru los celulares tienen 9 digitos y empiezan con 9
def validar_telefono_apoderado(telefono):
    telefono = telefono.strip()
    if telefono == "":
        return False, "El telefono del apoderado no puede estar vacio."
    if not telefono.isdigit():
        return False, "El telefono solo debe tener numeros."
    if len(telefono) != 9:
        return False, "El telefono debe tener 9 digitos."
    if telefono[0] != "9":
        return False, "El telefono debe empezar con 9."
    return True, ""


# Esta funcion le pide un dato al estudiante por la terminal.
# Si el dato esta mal, muestra el error y se lo vuelve a pedir
# hasta que lo escriba bien (eso es el while True).
def pedir_dato(mensaje, funcion_validar):
    while True:
        dato = input(mensaje)
        es_valido, error = funcion_validar(dato)
        if es_valido:
            print("   -> Dato valido\n")
            return dato.strip()
        print("   -> ERROR: " + error + "\n")


# Programa de prueba: solo corre si ejecutas este archivo directamente
# (si otro archivo lo importa, esto NO se ejecuta)
if __name__ == "__main__":
    print("=== REGISTRO DE ESTUDIANTE ===\n")

    nombre = pedir_dato("Nombre completo: ", lambda x: validar_no_vacio(x, "nombre"))
    dni = pedir_dato("DNI (8 digitos): ", validar_dni)
    fecha = pedir_dato("Fecha de nacimiento (DD/MM/AAAA): ", validar_fecha_nacimiento)
    nota = pedir_dato("Nota (0 a 20): ", validar_nota)
    telefono = pedir_dato("Telefono del apoderado (9 digitos): ", validar_telefono_apoderado)

    print("=== DATOS REGISTRADOS CORRECTAMENTE ===")
    print("Nombre:", nombre)
    print("DNI:", dni)
    print("Fecha de nacimiento:", fecha)
    print("Nota:", nota)
    print("Telefono del apoderado:", telefono)