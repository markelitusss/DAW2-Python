# Ejercicio 9 bloque 1 UD2

class Libro:
    total_libros = 0

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        Libro.total_libros += 1

    @classmethod
    def mostrar_total(cls):
        return "Total de libros: " + str(cls.total_libros)

    @staticmethod
    def es_formato_valido(formato):
        return formato in ("PDF", "EPUB", "PAPEL")
    
l1 = Libro("Harry Potter y la piedra filosofal", "JK Rowling")
l2 = Libro("El Señor de los Anillos", "JRR Tolkien")

print(Libro.mostrar_total()) # 2
print(l1.mostrar_total()) # 2
print(Libro.es_formato_valido("PDF")) # True
print(Libro.es_formato_valido("EXE")) # False
