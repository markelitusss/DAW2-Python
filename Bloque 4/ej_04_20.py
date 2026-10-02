# Ejercicio 20 bloque 4 UD1
alumnos = ["Julia", "Roberto", "Luis", "María", "Diego", "Alejandro"]
longitud_nombres = {n: len(n) for n in alumnos}
alumnos_largos = {n: len(n) for n in alumnos if len(n) >= 6}

print("Todos los alumnos:")
print(longitud_nombres)
print("Alumnos con nombre largo:")
print(alumnos_largos)