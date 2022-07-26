"""Pregunta 1"""

"""Nombre y edad en consola"""
nombre = input("¿Cuál es su nombre? ")
edad = int(input("¿Cuántos años tiene? "))

nombre2 = input("¿Cuál es su nombre? ")
edad2 = int(input("¿Cuántos años tiene? "))

print("Su nombre es {} y su edad es {}".format(nombre, edad))
print("El tipo de dato de nombre es {} y de edad es {}".format(type(nombre), type(edad)))

print("Su nombre es {} y su edad es {}".format(nombre2, edad2))
print("El tipo de dato de nombre es {} y de edad es {}".format(type(nombre2), type(edad2)))

print("La suma de las edad es: {}".format(edad + edad2))
