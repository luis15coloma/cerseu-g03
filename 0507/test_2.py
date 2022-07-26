"""Uso del for"""

ingenierias = ["Software", "Sistemas", "Industrial", "Electrónica", "Química"]
i = 0

print("El tamaño de nuestra lista es: {}".format(len(ingenierias)))
for ingenieria in ingenierias:


    print("Ingeniería {}".format(ingenieria))
    i = i + 1
    print("Esta es la vuelta número {}".format(i))
print("Llegó al final de nuestro for")