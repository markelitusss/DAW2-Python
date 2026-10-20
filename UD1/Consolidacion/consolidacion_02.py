# Ejercicio consolidación 2 UD1

catalogo = {
    "teclado": {"precio": 25.0, "stock": 10},
    "raton": {"precio": 15.0, "stock": 0},
    "monitor": {"precio": 120.0, "stock": 3},
    "auriculares": {"precio": 20.0, "stock": 5},
}
pedidos = [
    {"cliente": "Ana", "producto": "teclado", "cantidad": 2},
    {"cliente": "Luis", "producto": "raton", "cantidad": 1},
    {"cliente": "Marta", "producto": "monitor", "cantidad": 5},
    {"cliente": "Jon", "producto": "tablet", "cantidad": 1},
    {"cliente": "Eva", "producto": "auriculares", "cantidad": "dos"},
    {"cliente": "Pau", "producto": "teclado", "cantidad": 3},
]

def procesar_pedido(pedido: dict, catalogo: dict) -> float:
    producto = pedido["producto"]
    cantidad = pedido["cantidad"]
    
    if producto not in catalogo:
        raise ValueError("Producto no encontrado")
    
    if not isinstance(cantidad, int) or cantidad <= 0:
        raise ValueError("Cantidad inválida")
    
    info = catalogo[producto]
    if cantidad > info["stock"]:
        raise ValueError("Stock insuficiente")
    
    importe = cantidad * info["precio"]
    info["stock"] -= cantidad
    return importe
        
def recorrer_pedidos(pedidos: list) -> list:
    # - Pedidos aceptados
    # - Importe total
    # - Pedidos rechazados
    # - Rechazado por producto no encontrado
    # - Rechazado por cantidad inválida
    # - Rechazado por stock insuficiente
    datos = [0, 0, 0, 0, 0, 0]
    
    for i in pedidos:
        try:
            datos[1] += procesar_pedido(i, catalogo)
            datos[0] += 1
            print("Pedido de", i["cliente"], ": aceptado")
        except Exception as e:
            datos[2] += 1
            match str(e): # compara con el string del error
                case "Producto no encontrado":
                    datos[3] += 1
                case "Cantidad inválida":
                    datos[4] += 1
                case "Stock insuficiente":
                    datos[5] += 1
            
            print("Pedido de", i["cliente"], ": rechazado por", e)
    
    return datos

def recorrer_catalogo(cat: dict):
    print("\nStock final:")
    
    for producto, info in cat.items():
        print(producto, "->", info["stock"])

def main():
    datos = recorrer_pedidos(pedidos)
    
    print("\nPedidos aceptados:", datos[0])
    print("Importe total:", datos[1], "€")
    print("Pedidos rechazados:", datos[2])
    print("\tProducto no encontrado:", datos[3])
    print("\tCantidad inválida:", datos[4])
    print("\tStock insuficiente:", datos[5])
    
    recorrer_catalogo(catalogo)
    
if __name__ == "__main__":
    main()
    
