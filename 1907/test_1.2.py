"""Importación y uso de librerías"""
"""Uso específico de una funcionalidad para una librería o dependencia"""

from math import sqrt, pow
import math

numero = int(input("Por favor ingrese un número: "))

valorRaiz = sqrt(numero)
print("La raiz cuadrada de su número ingresado es: {}".format(valorRaiz))

valorPotencia = pow(5, 6)
print("El valor de mi potencia es: {}".format(valorPotencia))

print("Todas las funciones que tiene la librería math es: {}".format(dir(math)))
