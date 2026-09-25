# Ejercicio 5 Bloque 3 UD 1
import datetime

print ("MENU:")
print("1. Saludar")
print("2. Ver fecha")
print("3. Calcular cuadrado")
print("4. Salir")

num = int(input("Introduce una opción (1-4): "))

match num:
    case 1:
        print("Hola!")
    case 2:
        print("La fecha de hoy es", datetime.date.today())
    case 3:
        x = int(input("Introduce un número entero: "))
        print("El cuadrado de", x, "es", x ** 2)
    case 4:
        print("Adios!")
    case _:
        print("Opción no válida")