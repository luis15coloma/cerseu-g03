"""Bucle while"""

"""
- Leer por teclado enteros positivos hasta que el usuario ingrese -1
- Imprimir la suma de todos los digitos que lo componen

"""
numero = int(input("Ingrese un número positivo: "))
suma = 0
while numero != 0:
    digito = numero%10
    suma = suma + digito
    print("Dígito: {}".format(digito))
    print("Suma: {}".format(suma))
    numero = numero//10

    print("Número: {}".format(numero))
print("La suma de los digitos es: {}".format(suma))