"""Manejo de archivos"""
"""Apertura y lectura de archivos"""

"""r: Abre el archivo en modo de lectura"""

file = open("../my_files/files.txt", "r")
#file2.txt = open("file.docx", "r")
"""read()_ Nos permite leer el contenido de un archivo"""
print("Contenido de nuestro archivo 'files': {}".format(file.read()))
