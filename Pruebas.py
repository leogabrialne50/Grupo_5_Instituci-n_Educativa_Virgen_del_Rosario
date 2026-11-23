import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import almacenamiento
from consultas import buscar_recursivo, promedio_curso, promedio_general


class PruebasSistema(unittest.TestCase):

    def setUp(self):
        self.directorio = tempfile.TemporaryDirectory()
        self.archivo = Path(self.directorio.name) / "estudiantes.json"
        self.patch_archivo = patch.object(almacenamiento, "ARCHIVO", self.archivo)
        self.patch_archivo.start()

    def tearDown(self):
        self.patch_archivo.stop()
        self.directorio.cleanup()

    def estudiante_ejemplo(self):
        return {
            "dni": "12345678",
            "nombres": "Ana",
            "apellidos": "Perez",
            "notas": [
                {"curso": "Matematica", "bimestre": 1, "nota": 18},
                {"curso": "Matematica", "bimestre": 2, "nota": 16},
                {"curso": "Comunicacion", "bimestre": 1, "nota": 14}
            ]
        }

    def test_archivo_inexistente_devuelve_lista_vacia(self):
        self.assertEqual(almacenamiento.cargar_estudiantes(), [])

    def test_guardar_y_cargar_estudiantes(self):
        datos = [self.estudiante_ejemplo()]
        almacenamiento.guardar_estudiantes(datos)
        self.assertEqual(almacenamiento.cargar_estudiantes(), datos)

    def test_busqueda_recursiva_encuentra_dni(self):
        datos = [self.estudiante_ejemplo()]
        encontrado = buscar_recursivo(datos, "12345678")
        self.assertEqual(encontrado["nombres"], "Ana")

    def test_busqueda_recursiva_no_encuentra_dni(self):
        self.assertIsNone(buscar_recursivo([], "00000000"))

    def test_promedios(self):
        estudiante = self.estudiante_ejemplo()
        self.assertEqual(promedio_curso(estudiante, "Matematica"), 17)
        self.assertEqual(promedio_general(estudiante), 16)

    def test_json_danado_informa_error(self):
        self.archivo.write_text("{ archivo incorrecto", encoding="utf-8")
        with self.assertRaises(ValueError):
            almacenamiento.cargar_estudiantes()


if __name__ == "__main__":
    unittest.main(verbosity=2)
