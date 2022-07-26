"""Manejo de archivos"""

tecnologiasBackend = ["\nPython", "Java", "Ruby", "NodeJS"]
tecnologiasFrontend = ["\nAngular", "JavaScript", "ReactJS", "Boostrap"]

"""Apertura de nuestro archivo"""
"""a+: Permite escribir varias líneas al abrir nuestro archivo"""
"""a+: Escribe nuevas líneas de texto sin sobreescribir el contenido del archivo"""

file = open("my_files/files3.txt", "a+")

file.writelines(tecnologiasBackend)
file.writelines(tecnologiasFrontend)

file = open("my_files/files3.txt", "r")

print("El contenido de mi archivo es: {}".format(file.read()))

"""Cierre del archivo"""
file.close()