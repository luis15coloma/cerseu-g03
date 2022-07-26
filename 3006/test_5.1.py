"""Asignación múltiple"""
"""Referente a dos o más variables"""

nombre = input("Hola, ¿cuál es su nombre? ")
correo = input("Digite su correo electrónico ")
edad = input("¿Cuál es su edad? ")

nombreUsuario, correoUsuario, edadUsuario = nombre, correo, edad

print("El nombre del usuario es: {}".format(nombreUsuario))
print("Correo: {}".format(correoUsuario))
print("Su edad es: {}".format(edadUsuario))
