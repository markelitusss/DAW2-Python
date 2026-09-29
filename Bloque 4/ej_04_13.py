# Ejercicio 13 bloque 4 UD1
numeros = [1, 5, 6, 13, 14, 15, 28, 30, 35, 50]

# 1, 25, 36, 169, 196, 225, 784, 900, 1225, 2500
cuadrados = [n * n for n in numeros]

# 6, 14, 28, 30, 50
pares = [n for n in numeros if n % 2 == 0]

# 60, 140, 280, 300, 500
pares_x10 = [n * 10 for n in numeros if n % 2 == 0]