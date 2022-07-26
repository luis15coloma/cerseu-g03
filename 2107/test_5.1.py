"""Manejo de archivos"""

tecnologiasBackend = ["Python", "\nJava"]

file = open("my_files/file4.txt", "a+")

file.writelines(tecnologiasBackend)

file = open("my_files/file4.txt", "r")

for newLine in file:
    if newLine.find("Python"):
        print(newLine)
        print("Tienes en tu lista a Python")


"""Cierre del archivo"""
file.close()