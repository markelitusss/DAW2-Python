a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b) # true porque en la linea 2 se han igualado sus identidades
print(a is c) # false porque tienen identidades (direcciones de memoria) diferentes
print(a == c) # true porque su contenido es idéntico