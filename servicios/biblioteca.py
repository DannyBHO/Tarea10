import os
from modelo.libro import Libro


class Biblioteca:
    def __init__(self, archivo="biblioteca.txt"):
        self.archivo = archivo
        self.libros = []
        self.cargar_desde_archivo()

    # =====================
    # MANEJO DE ARCHIVOS
    # =====================

    def cargar_desde_archivo(self):
        try:
            if not os.path.exists(self.archivo):
                open(self.archivo, "w").close()
                print(" Archivo de biblioteca creado.")
                return

            with open(self.archivo, "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")

                    if len(datos) != 4:
                        print(" Línea corrupta ignorada.")
                        continue

                    id, titulo, autor, cantidad = datos
                    libro = Libro(id, titulo, autor, int(cantidad))
                    self.libros.append(libro)

            print(" Biblioteca cargada correctamente.")

        except FileNotFoundError:
            print(" Error: archivo no encontrado.")
        except PermissionError:
            print(" Error: sin permisos para leer.")
        except Exception as e:
            print(" Error inesperado:", e)

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for l in self.libros:
                    linea = f"{l.get_id()},{l.get_titulo()},{l.get_autor()},{l.get_cantidad()}\n"
                    f.write(linea)

            print(" Cambios guardados en archivo.")

        except PermissionError:
            print(" Error: sin permisos para escribir.")
        except Exception as e:
            print(" Error inesperado:", e)

    # =====================
    # FUNCIONES PRINCIPALES
    # =====================

    def añadir_libro(self, libro):
        for l in self.libros:
            if l.get_id() == libro.get_id():
                print(" Ya existe un libro con ese ID.")
                return

        self.libros.append(libro)
        self.guardar_en_archivo()
        print(" Libro añadido correctamente.")

    def eliminar_libro(self, id):
        for l in self.libros:
            if l.get_id() == id:
                self.libros.remove(l)
                self.guardar_en_archivo()
                print(" Libro eliminado.")
                return

        print(" Libro no encontrado.")

    def actualizar_libro(self, id, nueva_cantidad):
        for l in self.libros:
            if l.get_id() == id:
                l.set_cantidad(nueva_cantidad)
                self.guardar_en_archivo()
                print(" Libro actualizado.")
                return

        print(" Libro no encontrado.")

    def buscar_por_titulo(self, titulo):
        encontrados = [
            l for l in self.libros
            if titulo.lower() in l.get_titulo().lower()
        ]

        if encontrados:
            print("\n Resultados:")
            for l in encontrados:
                print(l)
        else:
            print(" No se encontraron libros.")

    def mostrar_biblioteca(self):
        if not self.libros:
            print(" Biblioteca vacía.")
            return

        print("\n LISTA DE LIBROS:")
        for l in self.libros:
            print(l)
