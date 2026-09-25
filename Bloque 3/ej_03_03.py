# Ejercicio 3 Bloque 3 UD 1

nota = float(input("Introduce una nota (0 - 10): "))

if nota < 0 or nota > 10:
    print("Nota no válida")
elif nota < 5:
    print("Suspenso")
elif nota < 6:
    print("Aprobado")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
elif nota <= 10:
    print("Sobresaliente")