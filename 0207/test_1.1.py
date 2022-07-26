"""Uso del flujo condicional if"""

edad = int(input("¿Cuál es su edad actual? "))
var1 = edad
var2 = 100.50
var3 = 30

if type(var1) == type(var3):
    print("El dato es tipo entero")
    resultado = var1 + 10
    print("La edad del usuario dentro de 10 años será: {}".format(resultado))
else:
    print("El dato ingresado por el ususario no es entero")