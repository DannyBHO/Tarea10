class Libro:
    def __init__(self, id, titulo, autor, cantidad):
        self._id = id
        self._titulo = titulo
        self._autor = autor
        self._cantidad = cantidad

    # Getters
    def get_id(self):
        return self._id

    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_cantidad(self):
        return self._cantidad

    # Setters
    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def __str__(self):
        return f"ID: {self._id} | Título: {self._titulo} | Autor: {self._autor} | Cantidad: {self._cantidad}"
