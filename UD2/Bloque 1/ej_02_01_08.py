# Ejercicio 8 bloque 1 UD2

class Libro:
    categoria = "Ficción"

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    

l1 = Libro("Harry Potter y la piedra filosofal", "JK Rowling")
l2 = Libro("El Señor de los Anillos", "JRR Tolkien")

# categoría inicial
print(l1.titulo, l1.autor, l1.categoria)
print(l2.titulo, l2.autor, l2.categoria)

Libro.categoria = "Fantasía"

# categoría después del cambio en la clase
print(l1.categoria, l2.categoria)

l1.categoria = "Ficción"

# categoría después del cambio en un objeto (se crea un atributo de instancia nuevo en el objeto modificado)
print(l1.categoria, l2.categoria, Libro.categoria)
