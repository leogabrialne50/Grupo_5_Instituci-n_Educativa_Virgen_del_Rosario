import json
from pathlib import Path

ARCHIVO = Path(__file__).resolve().parent / "estudiantes.json"


def cargar_estudiantes():
    """Devuelve la lista de estudiantes guardada en el archivo JSON."""
    if not ARCHIVO.exists():
        return []

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except json.JSONDecodeError as error:
        raise ValueError(
            "El archivo estudiantes.json esta dañado. "
            "No se modificaron los datos."
        ) from error
    except OSError as error:
        raise OSError("No se pudo leer estudiantes.json.") from error

    if not isinstance(datos, list):
        raise ValueError("El contenido de estudiantes.json debe ser una lista.")

    return datos

def guardar_estudiantes(estudiantes):
    """Guarda la lista completa usando un archivo temporal."""
    if not isinstance(estudiantes, list):
        raise TypeError("Los estudiantes deben estar organizados en una lista.")

    temporal=ARCHIVO.with_name(ARCHIVO.name + ".tmp")

    try:
        with open(temporal, "w", encoding="utf-8") as archivo:
            json.dump(estudiantes, archivo, ensure_ascii=False, indent=4)
            archivo.flush()

        temporal.replace(ARCHIVO)
    except OSError:
        if temporal.exists():
            temporal.unlink()
        raise
    