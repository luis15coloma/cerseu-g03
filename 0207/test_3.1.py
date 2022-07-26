"""Creación de una lista"""

"""Una variable que contenga 30 números aleatorios"""
"""Mostrar los valores al cuadrado y al cubo de la lista random"""
import random
listaRandom = []

for indice in range(1, 6):
    listaRandom.append(random.randint(5, 100))
print(listaRandom)

"""Obtener el tamaño de mi lista"""
print("El tamaño de mi lista es: {}".format(len(listaRandom)))

listaCuadrado = []
listaCubo = []
for valor in listaRandom:
    listaCuadrado.append(valor**2)
    listaCubo.append(valor**3)
print("El valor de la lista al cuadrado es: {}".format(listaCuadrado))
print("El valor de la lista al cubo es: {}".format(listaCubo))