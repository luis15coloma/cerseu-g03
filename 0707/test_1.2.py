"""Programación funcional"""

var1 = 50
var2 = 100
"""El nombre de la función en general es lo que va a realizar la función"""
"""Input: son los parámetros"""
def multiplicar(a, b):
    resultado = a*b
    return resultado    #Es el output: el valor que retorna la función
print("El resultado de mi función es: {}".format(multiplicar(var1,var2)))
