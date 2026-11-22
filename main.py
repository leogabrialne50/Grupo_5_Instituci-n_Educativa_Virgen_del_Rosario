 
import json
import os
from pathlib import Path
from datetime import datetime

ARCHIVO = Path(__file__).resolve().parent / "estudiantes.json"


def cargar_estudiantes():
    if not os.path.exists(ARCHIVO):
        return []

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)
            return datos if isinstance(datos, list) else []
    except (json.JSONDecodeError, OSError):
        print("No se pudo leer el archivo de datos.")
        return []


def guardar_estudiantes(estudiantes):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(estudiantes, f, ensure_ascii=False, indent=4)


def pedir_texto(mensaje):
    while True:
        dato = " ".join(input(mensaje).strip().split())

        if dato:
            return dato

        print("Este campo es obligatorio.")


def pedir_dni():
    while True:
        dni = input("DNI (8 digitos): ").strip()

        if dni.isdigit() and len(dni) == 8:
            return dni

        print("El DNI debe tener exactamente 8 digitos.")


def pedir_entero(mensaje, minimo, maximo):
    while True:
        try:
            numero = int(input(mensaje).strip())

            if minimo <= numero <= maximo:
                return numero

        except ValueError:
            pass

        print(f"Ingrese un entero entre {minimo} y {maximo}.")


def pedir_fecha():
    while True:
        fecha = input("Fecha de nacimiento (DD/MM/AAAA): ").strip()

        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            return fecha

        except ValueError:
            print("Fecha invalida. Use DD/MM/AAAA.")


def buscar_recursivo(estudiantes, dni, indice=0):
    if indice >= len(estudiantes):
        return None

    if estudiantes[indice]["dni"] == dni:
        return estudiantes[indice]

    return buscar_recursivo(estudiantes, dni, indice + 1)


def matricular():
    estudiantes = cargar_estudiantes()

    print("\n=== MATRICULA DE ESTUDIANTES ===")

    dni = pedir_dni()

    if buscar_recursivo(estudiantes, dni):
        print("Ese DNI ya esta matriculado. No se permiten duplicados.")
        return

    nombres = pedir_texto("Nombres: ").title()
    apellidos = pedir_texto("Apellidos: ").title()
    nacimiento = pedir_fecha()

    grado = pedir_entero("Grado (1 a 5): ", 1, 5)
    seccion = pedir_texto("Seccion: ").upper()
    anio = pedir_entero("Anio academico: ", 2020, 2100)

    apoderado = pedir_texto("Nombre del apoderado: ").title()

    while True:
        telefono = input("Telefono del apoderado: ").strip()

        if telefono.isdigit() and 7 <= len(telefono) <= 15:
            break

        print("Ingrese un telefono numerico de 7 a 15 digitos.")

    estudiante = {
        "dni": dni,
        "nombres": nombres,
        "apellidos": apellidos,
        "fecha_nacimiento": nacimiento,
        "grado": grado,
        "seccion": seccion,
        "anio_academico": anio,
        "apoderado": apoderado,
        "telefono": telefono,
        "estado": "Matriculado",
        "notas": [],
        "traslados": []
    }

    estudiantes.append(estudiante)
    guardar_estudiantes(estudiantes)

    print("Matricula registrada correctamente.")
def trasladar():
    estudiantes = cargar_estudiantes()

    print("\n=== TRASLADO DE ESTUDIANTE ===")

    dni = pedir_dni()
    estudiante = buscar_recursivo(estudiantes, dni)

    if estudiante is None:
        print("No se encontro al estudiante.")
        return

    if estudiante["estado"] != "Matriculado":
        print("El estudiante no se encuentra matriculado.")
        return

    print("\nDatos del estudiante:")
    print("Nombre:", estudiante["nombres"], estudiante["apellidos"])
    print("Grado:", estudiante["grado"])
    print("Seccion:", estudiante["seccion"])

    destino = pedir_texto("Institucion de destino: ").title()

    fecha = datetime.now().strftime("%d/%m/%Y")

    registro = {
        "fecha": fecha,
        "institucion_destino": destino,
        "estado_anterior": estudiante["estado"],
        "estado_nuevo": "Trasladado"
    }

    estudiante["traslados"].append(registro)
    estudiante["estado"] = "Trasladado"

    guardar_estudiantes(estudiantes)

    print("\nTraslado registrado correctamente.")
    print("Destino:", destino)
    print("Fecha:", fecha)
    print("Estado actualizado a: Trasladado")
if __name__ == "__main__":
    matricular()