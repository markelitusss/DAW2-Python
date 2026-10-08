# Ejercicio 9 bloque 4 UD1
a = {4, 6, 7, 1, 4}

# Conjunto sin repetidos -> {4, 6, 7, 1}
a = set(a)

b = {3, 4, 1, 9, 5}

# Unión -> todos los números -> 1, 3, 4, 5, 6, 7 y 9
# Intersección -> los números que están en los dos conjuntos -> 1 y 4
# Diferencia -> los números que están en el conjutno a pero no en b -> 6 y 7
print("Unión:", a | b)
print("Intersección:", a & b)
print("Diferencia:", a - b)