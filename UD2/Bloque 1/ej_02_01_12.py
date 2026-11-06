# Ejercicio 12 bloque 1 UD2

# Parte 1
class Producto:
    def __init__(self, precio):
        self.__precio = precio

    def get_precio(self):
        return self.__precio

    def set_precio(self, valor):
        if valor >= 0:
            self.__precio = valor

p1 = Producto(50)
print(p1.get_precio()) # 50
p1.set_precio(100)
p1.set_precio(-10)
print(p1.get_precio()) # 100

# Parte 2
class ProductoV2:
    def __init__(self, precio):
        self.precio = precio 

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor
    

# utiliza el getter o setter según la situación
p2 = ProductoV2(10)
p2.precio = 20

try:
    p2.precio = -10
except ValueError as error:
    print(error)

print(p2.precio) # 20