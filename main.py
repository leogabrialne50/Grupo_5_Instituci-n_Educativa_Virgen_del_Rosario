from Operaciones import matricular, registrar_nota, trasladar
from Consultas import buscar, ver_notas, listar, ordenar, resumen


def menu():
    print("\\n" + "=" * 52)
    print(" SISTEMA DE GESTION DE ESTUDIANTES - GRUPO 5")
    print(" MATRICULA | NOTAS | TRASLADO")
    print(" I.E. VIRGEN DEL ROSARIO - PILLO")
    print("=" * 52)
    print("1. Matricular estudiante")
    print("2. Buscar estudiante por DNI")
    print("3. Registrar notas")
    print("4. Ver notas y calcular promedios")
    print("5. Registrar traslado")
    print("6. Listar estudiantes")
    print("7. Ordenar estudiantes")
    print("8. Mostrar resumen")
    print("0. Salir")


def ejecutar():
    while True:
        menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            matricular()
        elif opcion == "2":
            buscar()
        elif opcion == "3":
            registrar_nota()
        elif opcion == "4":
            ver_notas()
        elif opcion == "5":
            trasladar()
        elif opcion == "6":
            listar()
        elif opcion == "7":
            ordenar()
        elif opcion == "8":
            resumen()
        elif opcion == "0":
            print("Gracias por utilizar el sistema.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    ejecutar()
