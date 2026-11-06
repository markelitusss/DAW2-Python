# Ejercicio 10 bloque 1 UD2

class Cuenta:
    def __init__(self, titular, saldo, codigo):
        self.titular = titular
        self._saldo = saldo
        self.__codigo = codigo

    def mostrar_saldo(self):
        print("Saldo en la cuenta:", self._saldo)
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print("Ingreso realizado correctamente")

    def retirar(self, cantidad, codigo):
        if codigo != self.__codigo:
            print("Clave incorrecta")
        elif cantidad <= 0 or cantidad > self._saldo:
            print("Cantidad no válida o saldo insuficiente")
        else:
            self._saldo -= cantidad
            print("Retiro completado")

c1 = Cuenta("Roberto", 100, "A12345")

c1.ingresar(50)
c1.retirar(25, "A12345")
c1.retirar(25, "B12345")
c1.mostrar_saldo()

# print(c1.__codigo) -> AttributeError: 'Cuenta' object has no attribute 'codigo'