# Grupo_5_Instituci-n_Educativa_Virgen_del_Rosario

Sistema de consola para gestionar estudiantes de la I.E. Virgen del Rosario - Pillo.

## Archivos por integrante

- `validaciones.py`: validación de datos (Integrante 1).
- `almacenamiento.py`: lectura y escritura del archivo JSON (Integrante 2).
- `consultas.py`: búsqueda, listado, ordenamiento y promedios (Integrante 3).
- `operaciones.py`: matrícula, registro de notas y traslados (Integrante 4).
- `main.py`: menú principal e integración de módulos (Integrante 5).
- `pruebas.py`: pruebas automatizadas del sistema (Integrante 5).

## Requisitos

Python 3.8 o superior. No requiere instalar paquetes externos.

## Ejecución

Desde la carpeta del proyecto:

```bash
python main.py
```

Los datos se guardan en `estudiantes.json` junto a los archivos Python.

## Ejecutar pruebas

```bash
python -m unittest pruebas.py -v
```

No subir al repositorio un archivo JSON que contenga datos personales reales.