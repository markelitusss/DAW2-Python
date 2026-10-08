# Ejercicio 17 bloque 3 UD 1

mensaje = "Esto es un mensaje de prueba"

def mostrar_mensaje():
    print(mensaje)

mostrar_mensaje()

def doble_numero(n):
    # doble está declarado dentro de esta funcion
    # no se puede acceder desde fuera
    doble = n * 2
    return doble

print(doble_numero(4))
del mensaje

# ahora la función mostrar_mensaje no puede accedar a la variable porque se ha borrado