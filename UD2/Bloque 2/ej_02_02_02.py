# Ejercicio 2 bloque 2 UD2

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        print("Soy", self.nombre)

class Empleado(Persona):
    def __init__(self, nombre, salario):
        super().__init__(nombre)
        self.salario = salario

    def presentarse(self):
        super().presentarse()
        print("Mi salario es", self.salario, "€")

p = Persona("Juan")
e = Empleado("Alberto", 1500)

p.presentarse()
e.presentarse()