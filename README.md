# Grupo_5_Instituci-n_Educativa_Virgen_del_Rosario

Sistema de consola para gestionar estudiantes de la I.E. Virgen del Rosario - Pillo.

## Archivos por integrante

- `validaciones.py`: validación de datos (JEAN).
- `almacenamiento.py`: lectura y escritura del archivo JSON (LEONARDO).
- `consultas.py`: búsqueda, listado, ordenamiento y promedios (SARA).
- `operaciones.py`: matrícula, registro de notas y traslados (ANAYELI).
- `main.py`: menú principal e integración de módulos (MARLON).
- `pruebas.py`: pruebas automatizadas del sistema (MARLONX2).

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