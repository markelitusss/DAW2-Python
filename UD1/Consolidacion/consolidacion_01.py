# Ejercicio consolidación 1 UD1

# Obtiene el nivel según la puntuación indicada
def obtener_nivel(puntuacion : float) -> str:
    nivel = ""

    # Error: la puntuación es menor a 0 o mayor a 100s
    if puntuacion < 0 or puntuacion > 100:
        raise ValueError("La puntuación de la prueba debe estar entre 0 y 100\n")

    if puntuacion < 40:
        nivel = "Principiante"
    elif puntuacion > 40 and puntuacion < 75:
        nivel = "Intermedio"
    else:
        nivel = "Avanzado"

    return nivel

# Inicio ejecución programa
def main():

    # Variables
    sumPrincipiante = 0
    sumIntermedio = 0
    sumAvanzado = 0
    inscripciones = [] # lista de diccionarios

    # Bucle principal del programa
    while True:
        nombre = input("Introduce el nombre: ")

        # se acaba el bucle
        if nombre.lower() == "fin":
            break

        edad = 0
        # el usuario introduce un valor hasta que sea un entero
        while True:
            try:
                edad = int(input("Introduce la edad: "))
                break
            except Exception:
                print("Entrada no válida, vuelve a intentarlo")

        puntuacion = 0
        # el usuario introduce un valor hasta que sea entero o decimal
        while True:
            try:
                puntuacion = float(input("Introduce la puntuación obtenida en la prueba: "))
                break
            except Exception:
                print("Entrada no válida, vuelve a intentarlo")

        # parte final del bucle
        # se obtiene el nivel en base a la puntuación introducida
        try:
            nivel = obtener_nivel(puntuacion)
            match nivel:
                case "Principiante":
                    sumPrincipiante += 1
                case "Intermedio":
                    sumIntermedio += 1
                case "Avanzado":
                    sumAvanzado += 1

            # si no quedan plazas se lanza una excepción
            if sumPrincipiante > 2 or sumIntermedio > 2 or sumAvanzado > 1:
                raise IndexError

            # se realiza la inscripción
            inscripciones.append({"nombre": nombre, "edad": edad, "puntuacion": puntuacion, "nivel": nivel})
            print("Inscripción registrada correctamente con nivel:", nivel, "\n")
        # Error: véase obtener_nivel()
        except ValueError as e:
            print(e)
        # Error: no quedan plazas en un nivel
        except IndexError:
            print("Inscripción rechazada: no quedan plazas en el nivel solicitado\n")
            
            # se revierte el contador al valor anterior a la inscripción fallida
            match nivel:
                case "Principiante":
                    sumPrincipiante -= 1
                case "Intermedio":
                    sumIntermedio -= 1
                case "Avanzado":
                    sumAvanzado -= 1
        
    # Resumen final
    print("\nNúmero total de personas inscritas:", len(inscripciones))
    print("Inscripciones nivel principiante:", sumPrincipiante)
    print("Inscripciones nivel intermedio:", sumIntermedio)
    print("Inscripciones nivel avanzado:", sumAvanzado)

if __name__ == "__main__":
    main()