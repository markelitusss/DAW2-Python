# Ejercicio 14 bloque 5 UD1

# Función de celsius a fahrenheit
def celsiusFahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32

# Función de fahrenheit a celsius
def fahrenheitCelsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9

# Función principal
def main():
    try:
        tipo = input("Celsius o Fahrenheit? (C/F): ")
        grados = float(input("Introduce el número de grados: "))

        if tipo == 'C':
            print("Resultado:", round(celsiusFahrenheit(grados), 2), "grados Fahrenheit")
        elif tipo == 'F':
            print("Resultado:", round(fahrenheitCelsius(grados), 2), "grados Celsius")
        else:
            raise TypeError
    except ValueError:
        print("Error: los grados deben ser un número")
    except TypeError:
        print("Error: letra errónea")

if __name__ == "__main__":
    main()