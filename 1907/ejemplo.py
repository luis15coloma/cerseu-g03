import random

"""Funcion para generar números aleatorios"""
lista = []
for i in range(3):
    num = random.randint(1,5)
    lista.append(num)
print(lista)