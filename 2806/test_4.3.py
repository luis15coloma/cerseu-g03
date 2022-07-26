"""Estructura de datos"""

"""Lista: quitar un item por su indice"""

lista = ["Día de la bandera", True, 2000, 40.9]

"""Usando el pop"""
lista.pop(1)
lista.append(False)
lista.append(8000)

lista.pop(0)
print("Nuestra nueva lista es: {}".format(lista))

