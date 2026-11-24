from Almacenamiento import cargar_estudiantes, guardar_estudiantes
from Validaciones import pedir_dni


def buscar_recursivo(estudiantes, dni, indice=0):
    """Busca un estudiante por DNI mediante recursividad."""
    if indice >= len(estudiantes):
        return None
    if estudiantes[indice]["dni"] == dni:
        return estudiantes[indice]
    return buscar_recursivo(estudiantes, dni, indice + 1)


def promedio_curso(estudiante, curso):
    notas = [
        nota["nota"] for nota in estudiante["notas"]
        if nota["curso"].casefold() == curso.casefold()
    ]
    return sum(notas) / len(notas) if notas else None


def promedio_general(estudiante):
    notas = [nota["nota"] for nota in estudiante["notas"]]
    return sum(notas) / len(notas) if notas else None


def obtener_estudiante(estudiantes=None):
    if estudiantes is None:
        estudiantes = cargar_estudiantes()

    if not estudiantes:
        print("No hay estudiantes registrados.")
        return None

    dni = pedir_dni()
    estudiante = buscar_recursivo(estudiantes, dni)

    if estudiante is None:
        print("No se encontro al estudiante.")

    return estudiante


def mostrar_estudiante(estudiante):
    print("\\n--- DATOS DEL ESTUDIANTE ---")
    print(f"DNI: {estudiante['dni']}")
    print(f"Nombres: {estudiante['nombres']} {estudiante['apellidos']}")
    print(f"Nacimiento: {estudiante['fecha_nacimiento']}")
    print(f"Grado y seccion: {estudiante['grado']} - {estudiante['seccion']}")
    print(f"Anio academico: {estudiante['anio_academico']}")
    print(f"Apoderado: {estudiante['apoderado']} | Telefono: {estudiante['telefono']}")
    print(f"Estado: {estudiante['estado']}")
    promedio = promedio_general(estudiante)
    print("Promedio general:", f"{promedio:.2f}" if promedio is not None else "Sin notas")


def buscar():
    estudiante = obtener_estudiante()
    if estudiante:
        mostrar_estudiante(estudiante)


def ver_notas():
    estudiante = obtener_estudiante()
    if estudiante is None:
        return

    if not estudiante["notas"]:
        print("El estudiante aun no tiene notas.")
        return

    cursos = []
    for nota in estudiante["notas"]:
        if nota["curso"].casefold() not in [curso.casefold() for curso in cursos]:
            cursos.append(nota["curso"])

    print(f"\\nNOTAS: {estudiante['nombres']} {estudiante['apellidos']}")
    for curso in cursos:
        print(f"\\n{curso}")
        for nota in estudiante["notas"]:
            if nota["curso"].casefold() == curso.casefold():
                print(f"  Bimestre {nota['bimestre']}: {nota['nota']:g}")
        promedio = promedio_curso(estudiante, curso)
        print(f"  Promedio del curso: {promedio:.2f}")

    print(f"PROMEDIO GENERAL: {promedio_general(estudiante):.2f} / 20")


def listar():
    estudiantes = cargar_estudiantes()
    if not estudiantes:
        print("No hay estudiantes.")
        return

    for estudiante in estudiantes:
        resultado = promedio_general(estudiante)
        promedio = f"{resultado:.2f}" if resultado is not None else "Sin notas"
        print(
            f"{estudiante['dni']} | {estudiante['apellidos']}, "
            f"{estudiante['nombres']} | Grado {estudiante['grado']}"
            f"{estudiante['seccion']} | {estudiante['estado']} | "
            f"Promedio: {promedio}"
        )


def ordenar():
    estudiantes = cargar_estudiantes()
    if not estudiantes:
        print("No hay estudiantes.")
        return

    print("1. Apellidos  2. Grado  3. Promedio")
    opcion = input("Criterio: ").strip()

    if opcion == "1":
        estudiantes.sort(key=lambda e: e["apellidos"].casefold())
    elif opcion == "2":
        estudiantes.sort(key=lambda e: (e["grado"], e["seccion"].casefold()))
    elif opcion == "3":
        estudiantes.sort(
            key=lambda e: (
                promedio_general(e) is None,
                -(promedio_general(e) or 0)
            )
        )
    else:
        print("Opcion no valida.")
        return

    guardar_estudiantes(estudiantes)
    print("Listado ordenado:")
    for estudiante in estudiantes:
        resultado = promedio_general(estudiante)
        promedio = f"{resultado:.2f}" if resultado is not None else "Sin notas"
        print(
            f"{estudiante['dni']} | {estudiante['apellidos']}, "
            f"{estudiante['nombres']} | Grado {estudiante['grado']}"
            f"{estudiante['seccion']} | {estudiante['estado']} | "
            f"Promedio: {promedio}"
        )


def resumen():
    estudiantes = cargar_estudiantes()
    if not estudiantes:
        print("No hay datos.")
        return

    matriculados = sum(1 for e in estudiantes if e["estado"] == "Matriculado")
    trasladados = sum(1 for e in estudiantes if e["estado"] == "Trasladado")
    print(
        f"Total: {len(estudiantes)} | Matriculados: {matriculados} | "
        f"Trasladados: {trasladados}"
    )

    # Arreglos paralelos: cada indice relaciona DNI, nombre y promedio.
    dnis, nombres, promedios = [], [], []
    for estudiante in estudiantes:
        dnis.append(estudiante["dni"])
        nombres.append(estudiante["nombres"] + " " + estudiante["apellidos"])
        promedios.append(promedio_general(estudiante))

    for indice in range(len(dnis)):
        promedio = (
            f"{promedios[indice]:.2f}"
            if promedios[indice] is not None else "Sin notas"
        )
        print(f"{dnis[indice]} | {nombres[indice]} | {promedio}")
