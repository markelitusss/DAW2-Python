altura = float(input("Introduce tu altura en metros: "))
peso = float(input("Introduce tu peso en kilogramos: "))

print("Altura: ", altura, type(altura))
print("Peso: ", peso, type(peso))
print("IMC: ", round(peso / (altura ** 2), 2))
