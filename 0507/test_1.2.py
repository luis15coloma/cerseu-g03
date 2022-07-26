"""Bucle while"""
"""
 - Ingresar números enteros por teclado hasta que el usuario ingrese 1
 - Realizar la sumatoria de todos los números ingresados
"""
numero = int(input("Ingrese un número: "))

total = 0
while numero != 1:
    total = total + numero
    print("Mi suma hasta el momento es: {}".format(total))
    numero = int(input("Ingrese un número: "))

print("La sumatoria de todos los números ingresados es: {}".format(total))