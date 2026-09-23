a = int(input("Introduce un número: "))
b = int(input("Introduce otro número: "))

print("Valores iniciales: a = ", a, " b = ", b)

a, b = b, a

print("Valores sin tercera variable: a = ", a, " b = ", b)

a, b = b, a

temp = a
a = b
b = temp
print("Valores con tercera variable: a = ", a, "b = ", b)