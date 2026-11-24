from datetime import datetime


def pedir_texto(mensaje):
    while True:
        dato = " ".join(input(mensaje).strip().split())

        if dato:
            return dato

        print("Este campo no puede estar vacio.")


def validar_dni():
    while True:
        dni = input("DNI (8 digitos): ").strip()

        if not dni:
            print("El DNI no puede estar vacio.")
        elif not dni.isdigit():
            print("El DNI solo debe tener numeros.")
        elif len(dni) != 8:
            print("El DNI debe tener exactamente 8 digitos.")
        else:
            return dni


# Alias para compatibilidad con archivos que importen 'pedir_dni'
pedir_dni = validar_dni


def pedir_entero(mensaje, minimo, maximo):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("El campo no puede estar vacio.")
            continue

        if not texto.isdigit():
            print("El campo solo acepta numeros.")
            continue

        numero = int(texto)

        if minimo <= numero <= maximo:
            return numero
        print(f"El numero debe estar entre {minimo} y {maximo}.")


def pedir_fecha():
    while True:
        fecha = input("Fecha de nacimiento (DD/MM/AAAA): ").strip()

        if not fecha:
            print("La fecha de nacimiento no puede estar vacia.")
            continue

        try:
            fecha_validada = datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError:
            print("Fecha invalida. Usa el formato DD/MM/AAAA (ejemplo: 15/03/2010).")
            continue

        hoy = datetime.now()

        if fecha_validada > hoy:
            print("La fecha de nacimiento no puede ser futura.")
            continue

        edad = hoy.year - fecha_validada.year

        if (hoy.month, hoy.day) < (fecha_validada.month, fecha_validada.day):
            edad -= 1

        if edad < 3 or edad > 25:
            print("La edad debe estar entre 3 y 25 anios para un estudiante.")
            continue

        return fecha


def pedir_nota():
    while True:
        dato = input("Nota (0 a 20): ").strip()

        if not dato:
            print("La nota no puede estar vacia.")
            continue

        try:
            nota = float(dato.replace(",", "."))
        except ValueError:
            print("La nota debe ser un numero.")
            continue

        if not 0 <= nota <= 20:
            print("La nota debe estar entre 0 y 20.")
            continue

        return nota


# 6. Validar el telefono del apoderado
# En Peru los celulares tienen 9 digitos y empiezan con 9
def pedir_telefono():
    while True:
        telefono = input("Telefono del apoderado: ").strip()

        if not telefono:
            print("El telefono del apoderado no puede estar vacio.")
        elif not telefono.isdigit():
            print("El telefono solo debe tener numeros.")
        elif len(telefono) != 9:
            print("El telefono debe tener 9 digitos.")
        elif not telefono.startswith("9"):
            print("El telefono debe empezar con 9.")
        else:
            return telefono
