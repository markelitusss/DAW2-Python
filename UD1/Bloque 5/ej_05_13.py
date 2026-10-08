# Ejercicio 13 bloque 5 UD1
# Cogemos el programa del ejercicio 10 y le añadimos anotaciones de tipos
# a las funciones celsiusFahrenheit y fahrenheitCelsius

# Función de celsius a fahrenheit
def celsiusFahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32

# Función de fahrenheit a celsius
def fahrenheitCelsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9

# Función principal
def main():
    tipo = input("Celsius o Fahrenheit? (C/F): ")
    grados = float(input("Introduce el número de grados: "))

    if tipo == 'C':
        print("Resultado:", celsiusFahrenheit(grados), "grados Fahrenheit")
    elif tipo == 'F':
        print("Resultado:", fahrenheitCelsius(grados), "grados Celsius")
    else:
        print("Error: no se ha escogido C o F")

if __name__ == "__main__":
    main()