from modelo.libro import Libro
from servicios.biblioteca import Biblioteca

biblioteca = Biblioteca()


def menu():
    while True:
        print("\n===== SISTEMA DE BIBLIOTECA =====")
        print("1. Añadir libro")
        print("2. Eliminar libro")
        print("3. Actualizar cantidad")
        print("4. Buscar por título")
        print("5. Mostrar biblioteca")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id = input("ID: ")
                titulo = input("Título: ")
                autor = input("Autor: ")
                cantidad = int(input("Cantidad: "))

                libro = Libro(id, titulo, autor, cantidad)
                biblioteca.añadir_libro(libro)

            elif opcion == "2":
                id = input("ID a eliminar: ")
                biblioteca.eliminar_libro(id)

            elif opcion == "3":
                id = input("ID del libro: ")
                cantidad = int(input("Nueva cantidad: "))
                biblioteca.actualizar_libro(id, cantidad)

            elif opcion == "4":
                titulo = input("Título a buscar: ")
                biblioteca.buscar_por_titulo(titulo)

            elif opcion == "5":
                biblioteca.mostrar_biblioteca()

            elif opcion == "6":
                print(" Saliendo del sistema...")
                break

            else:
                print(" Opción inválida.")

        except ValueError:
            print(" Error: ingreso numérico inválido.")


if __name__ == "__main__":
    menu()
