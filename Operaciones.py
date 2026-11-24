
import json
from pathlib import Path
from datetime import datetime

ARCHIVO = Path(__file__).resolve().parent / "estudiantes.json"


# Cargar y guardar estudiantes
def cargar_estudiantes():
    if not ARCHIVO.exists():
        return []

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        return datos if isinstance(datos, list) else []

    except (json.JSONDecodeError, OSError):
        print("No se pudo leer el archivo de datos.")
        return []


def guardar_estudiantes(estudiantes):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(estudiantes, archivo, ensure_ascii=False, indent=4)


# Validar datos
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

        print(f"Ingrese un numero entre {minimo} y {maximo}.")


def pedir_fecha():
    while True:
        fecha = input("Fecha de nacimiento (DD/MM/AAAA): ").strip()

        try:
            fecha_validada = datetime.strptime(fecha, "%d/%m/%Y")

            if fecha_validada.date() > datetime.now().date():
                print("La fecha no puede ser futura.")
                continue

            return fecha

        except ValueError:
            print("Fecha invalida. Use DD/MM/AAAA.")


def pedir_nota():
    while True:
        try:
            nota = float(input("Nota (0 a 20): ").strip().replace(",", "."))

            if 0 <= nota <= 20:
                return nota

        except ValueError:
            pass

        print("La nota debe estar entre 0 y 20.")


# Buscar estudiante mediante recursividad
def buscar_recursivo(estudiantes, dni, indice=0):
    if indice >= len(estudiantes):
        return None

    if estudiantes[indice]["dni"] == dni:
        return estudiantes[indice]

    return buscar_recursivo(estudiantes, dni, indice + 1)


# Matricula de estudiantes
def matricular():
    estudiantes = cargar_estudiantes()

    print("\nMATRICULA DE ESTUDIANTES")

    dni = pedir_dni()

    if buscar_recursivo(estudiantes, dni):
        print("Ese DNI ya esta registrado.")
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

        if telefono.isdigit() and len(telefono) == 9 and telefono.startswith("9"):
            break

        print("Ingrese un telefono de 9 digitos que empiece con 9.")

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

    print("\nMatricula registrada correctamente.")
    print("Estudiante:", nombres, apellidos)


# Registro de notas
def registrar_nota():
    estudiantes = cargar_estudiantes()

    print("\nREGISTRO DE NOTAS")

    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    dni = pedir_dni()
    estudiante = buscar_recursivo(estudiantes, dni)

    if estudiante is None:
        print("No se encontro al estudiante.")
        return

    if estudiante.get("estado") != "Matriculado":
        print("El estudiante no esta matriculado.")
        return

    print("\nEstudiante:", estudiante["nombres"], estudiante["apellidos"])

    curso = pedir_texto("Nombre del curso: ").title()
    bimestre = pedir_entero("Bimestre (1 a 4): ", 1, 4)

    notas = estudiante.setdefault("notas", [])

    for registro in notas:
        if (
            registro["curso"].casefold() == curso.casefold()
            and registro["bimestre"] == bimestre
        ):
            print("Ya existe una nota para ese curso y bimestre.")
            return

    nota = pedir_nota()

    registro = {
        "curso": curso,
        "bimestre": bimestre,
        "nota": nota
    }

    notas.append(registro)
    guardar_estudiantes(estudiantes)

    print("\nNota registrada correctamente.")
    print("Curso:", curso)
    print("Bimestre:", bimestre)
    print("Nota:", nota)


# Traslado de estudiantes
def trasladar():
    estudiantes = cargar_estudiantes()

    print("\nTRASLADO DE ESTUDIANTES")

    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    dni = pedir_dni()
    estudiante = buscar_recursivo(estudiantes, dni)

    if estudiante is None:
        print("No se encontro al estudiante.")
        return

    if estudiante.get("estado") != "Matriculado":
        print("El estudiante no esta matriculado.")
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

    estudiante.setdefault("traslados", []).append(registro)
    estudiante["estado"] = "Trasladado"

    guardar_estudiantes(estudiantes)

    print("\nTraslado registrado correctamente.")
    print("Destino:", destino)
    print("Fecha:", fecha)
    print("Estado actualizado: Trasladado")
