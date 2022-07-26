"""Uso del flujo condicional if"""

edad = int(input("¿Cuál es su edad?: "))

if 0 < edad < 18:
    print("Es usted menor de edad")
elif 18 <= edad <= 65:
    print("Usted es mayor de edad")
elif 65 < edad < 120:
    print("Usted es una persona de la tercera edad")
else:
    print("La edad ingresada es errada")

