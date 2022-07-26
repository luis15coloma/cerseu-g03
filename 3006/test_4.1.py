"""E/S Python"""

"""Entradas en Python"""

usuario = input("Ingrese el nombre del usuario ")
nombre = input("¿Cuál es su nombre ")

print("Bienvenido {}".format(nombre))

telefono = input("Ingrese su número de celular: ")
print("{} tiene el número de celular {}".format(nombre, telefono))

edad = int(input("¿Cuál es su edad?: "))
print(type(edad))
print("Usted tiene {} años".format(edad))
