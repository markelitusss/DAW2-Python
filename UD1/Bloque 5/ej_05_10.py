# Ejercicio 10 bloque 5 UD1

# Función de celsius a fahrenheit
def celsiusFahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# Función de fahrenheit a celsius
def fahrenheitCelsius(fahrenheit):
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
