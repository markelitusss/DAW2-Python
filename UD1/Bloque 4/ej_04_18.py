# Ejercicio 18 bloque 4 UD1
notas = [5.5, 7, 8.5, 4.25, 2.5, 9, 9.5, 8.75, 6, 6.75]
notas_redondeadas = [round(n) for n in notas]

# unifica las dos listas
mensajes = list(zip(notas, notas_redondeadas))

print("Lista original:")
print(notas)
print("Lista de notas redondeadas")
print(notas_redondeadas)
print("Lista de mensajes:")
for nota, nota_redondeada in mensajes:
    print("Nota original ->", nota, "Nota redondeada ->", nota_redondeada)