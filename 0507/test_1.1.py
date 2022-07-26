"""Bucle while"""

numero = int(input("Ingrese un número menor que 10: "))

while numero < 10:
    numero += 1 #Aumenta en 1 a la variable numero
    print("El número es: {}".format(numero))
    if numero == 8:
        print("Número encontrado!")
        break       #Break nos permite romper el bucle antes de que llegue al tope de la condición


print("Llego al final del bucle while")