# Ejercicio 4 bloque 4 UD1
palabra = input("Introduce una palabra: ")
palabra_lower = palabra.lower()

if palabra_lower[::-1] == palabra_lower:
    print("La palabra " + palabra + " es un palíndromo")
else:
    print("La palabra " + palabra + " NO es un palíndromo")