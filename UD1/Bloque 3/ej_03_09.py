# Ejercicio 9 bloque 3 UD 1

suma = 0

while True:
    num = int(input("Introduce un número entero: "))
    if (num > 0):
        suma += num
    elif (num < 0):
        print("Número ignorado")
        continue
    else:
        break

print("Suma total:", suma)