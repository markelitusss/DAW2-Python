# Ejercicio 8 bloque 2 UD2

from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


c = Cuadrado(5)
r = Rectangulo(6, 2)
def mostrar_area(figura):
    print(figura.area())

mostrar_area(c)
mostrar_area(r)

try:
    f = Figura()
except Exception as e:
    print(e)