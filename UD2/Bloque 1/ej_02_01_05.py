# Ejercicio 5 bloque 1 UD2

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def presentar(self):
        print("El libro '" + self.titulo + "' ha sido escrito por", self.autor)


l1 = Libro("Harry Potter y la piedra filosofal", "JK Rowling")
l2 = Libro("El Señor de los Anillos", "JRR Tolkien")
# l3 = Libro() -> TypeError: Libro.__init__() missing 2 required positional arguments: 'titulo' and 'autor'

l1.presentar()
l2.presentar()
