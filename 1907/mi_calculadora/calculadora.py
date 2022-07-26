"""Funcion principal"""
"Llama a las demas funciones de mi modulo externo"

from funciones import suma, multiplicacion

x = int(input("Ingrese un valor: "))
y = int(input("Ingrese un segundo valor: "))

sum = suma(x, y)
print("El resultado de la suma de los dos valores ingresados es: {}".format(sum))

mul = multiplicacion(x, y)
print("El resultado de la multiplicación de los dos valores ingresados es: {}".format(mul))

print("El resultado de la multiplicación de los dos valores ingresados es: {}".format(resta(x, y)))
