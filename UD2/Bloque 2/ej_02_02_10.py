# Ejercicio 10 bloque 2 UD2

class SaldoInsuficienteError(Exception):
    pass

class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("Cantidad de retiro no válida")
        elif cantidad > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente: " + str(self._saldo) + " €")
        else:
            self._saldo -= cantidad
            print("Retirada exitosa")

c = Cuenta(100)

try:
    c.retirar(50)
    c.retirar(-10)
except ValueError as error:
    print(error)

try:
    c.retirar(100)
except SaldoInsuficienteError as error:
    print(error)

print("Saldo final", c._saldo)
