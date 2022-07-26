import random

"""Función para pedir un número"""


def cargar():
    return int(input("Ingrese un número: "))


"""Función para obtener un número aleatorio"""


def cargarAleatorio():
    return random.randint(1, 40)


"""Función para divinar al número"""


def adivinaNumero():
    numero = cargarAleatorio()
    print("Bienvenido al juego de adivina el número")

    esNumero = False
    while esNumero == False:
        x = cargar()
        if numero == x:
            print("¡Has ganado!")
            esNumero = True
        elif numero < x:
            print("El valor ingresado es menor")
        else:
            print("El valor es mayor")