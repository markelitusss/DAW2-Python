# Ejercicio 7 bloque 2 UD2

class Email:
    def enviar(self, mensaje):
        print(mensaje)

class SMS:
    def enviar(self, mensaje):
        print(mensaje)

class Notificacion:
    def enviar(self, mensaje):
        print(mensaje)

class Test:
    def error(self):
        print("Error")

def avisar(canales, mensaje):
    for i in canales:
        i.enviar(mensaje)

e = Email()
s = SMS()
n = Notificacion()
t = Test()
avisar([e, s, n], "Hola!")
# el programa funciona porque en Python el polimorfismo no exige herencia
# si añadimos el objeto t -> AttributeError