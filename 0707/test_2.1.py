"""Problema 01"""

"""
- Pedir al usuario su email y mostrarlo por pantallaindicando que es su dirección
- Validar si es una dirección de correo electrónico
- El email se considerará si tiene el simbolo del arroba '@'
"""

def validar(email):
    caracterPedido = "@"
    for letra in email:
        if letra == caracterPedido:
            return True
    return False

emailUsuario = input("Ingrse su email por favor: ")

if validar(emailUsuario):
    print("Email válido")
else:
    print("Email incorrecto")