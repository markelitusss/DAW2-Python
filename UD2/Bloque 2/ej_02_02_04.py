# Ejercicio 4 bloque 2 UD2

class Online:
    def tipo(self):
        print("Visita online")

class Presencial:
    def tipo(self):
        print("Visita presencial")

class VisitaMixta(Online, Presencial):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        print("Nombre de la visita:", self.nombre)
        print(self.tipo())

v = VisitaMixta("Visita 1")

# mostrar_info() busca la primera función tipo() que encuentre en base al MRO (Method Resolution Order)
v.mostrar_info()
print(VisitaMixta.mro())
Presencial.tipo(v)
