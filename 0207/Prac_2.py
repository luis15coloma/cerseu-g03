"""Pregunta 2"""

"""Listas random"""
import random

lista1 =[]

for valor in range (1, 11):
    lista1.append(random.randint(1, 20))

lista3 = []
lista2 = []
for val in lista1:
    lista3.append(val ** 3)
    lista2.append(val**2)

Sumlista = lista3 + lista2
Sumlista.reverse()
print(Sumlista)
