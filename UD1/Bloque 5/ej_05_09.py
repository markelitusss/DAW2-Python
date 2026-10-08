# Ejercicio 9 bloque 5 UD1
# variables
num1 = 0
num2 = 0
operador = ""
contOperaciones = 0
contErrores = 0

# bucle del programa
while (True):
    num1 = input("Introduce el primer número: ")
    num1 = num1.lower()

    if (num1 == "salir"):
        break

    num2 = input("Introduce el segundo número: ")

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Entrada no válida")
        contErrores += 1
        continue

    try:
        operador = input("Introduce un operador (+, -, *, /): ")

        match (operador):
            case '+':
                print(num1, "+", num2, "=", num1 + num2)
            case '-':
                print(num1, "-", num2, "=", num1 - num2)
            case '*':
                print(num1, "*", num2, "=", num1 * num2)
            case '/':
                print(num1, "/", num2, "=", num1 / num2)
            case _:
                raise ValueError

        contOperaciones += 1

    except ValueError:
        print("Operador no válido")
        contErrores += 1
    except ZeroDivisionError:
        print("Intento de división por 0 neutralizado")
        contErrores += 1
        
print("Número de operaciones realizadas:", contOperaciones)
print("Número de errores controlados:", contErrores)