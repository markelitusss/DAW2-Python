# Ejercicio 6 bloque 2 UD2

class Transporte:
    def salir(self):
        print("Saliendo...")

class Autobus:
    def salir(self):
        print("Saliendo (en autobús)...")

class Barco:
    def salir(self):
        print("Saliendo (en barco)...")

class Tren(Transporte):
    def salir(self):
        print("Saliendo (en tren)...")

def iniciar_viaje(transportes):
    for i in transportes:
        i.salir()

t = Transporte()
a = Autobus()
b = Barco()
tr = Tren()

iniciar_viaje([t, a, b, tr])