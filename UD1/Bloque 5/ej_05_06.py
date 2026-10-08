# Ejercicio 6 bloque 5 UD1
try:
    num = int(input("Introduce un número entero: "))
except ValueError:
    print("Entrada no válida")
else:
    print("Número correcto")
finally:
    print("Fin del intento de lectura")
