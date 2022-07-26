"""Estructura de datos"""

"""Eliminando un key de un diccionario"""

diccionario = {"nombre": "Python", "tipo": "Backend"}

print("El valor de mi variable diccionario es: {}".format(diccionario))

del diccionario["tipo"]
print("Mi diccionario actualizado es: {}".format(diccionario))

del diccionario["nombre"]
print("Mi diccionario actualizado por segunda vez es: {}".format(diccionario))