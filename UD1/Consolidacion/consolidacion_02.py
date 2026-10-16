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

def procesar_pedido(pedido: dict) -> float:
    if pedido["producto"] not in catalogo:
        raise ValueError("Producto no encontrado")
    elif pedido["cantidad"] <= 0:
        try:
            int(pedido["cantidad"])
        except Exception:
            print("Cantidad inválida")
        else:
            raise ValueError("Cantidad inválida")
    elif pedido["cantidad"] > catalogo[pedido["producto"]["stock"]]:
        raise ValueError("Stock insuficiente")
    else:
        importe = pedido["cantidad"] * catalogo[pedido["producto"]["precio"]]
        catalogo[pedido["producto"]["stock"]] -= pedido["cantidad"]
        return importe
        
# WIP
