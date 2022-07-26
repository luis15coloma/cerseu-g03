"Introducción a los diccionarios"

"Declarando nuestro primer diccionario"

diccionario = {"nombre": "Carlos", "apellido": "Fernandez", "edad": 29}

print("El contenido de mi variable diccionario es: {}".format(diccionario))

print(diccionario['nombre'])

print("Bienvenido {} {}, usted tiene {} años".format(diccionario['nombre'], diccionario ['apellido'], diccionario ['edad']))

diccionario2 = {"nombre": "Andrea", "apellido": "Monzón", "cursos": ["Python", "Django", "UX"]}

print("Los cursos en los que está matriculada son: {}".format(diccionario2['cursos']))

print("1er curso {}".format(diccionario2['cursos'][0]))
print("2er curso {}".format(diccionario2['cursos'][1]))
print("3er curso {}".format(diccionario2['cursos'][2]))

i=0
for key in diccionario2:
    if key == 'cursos':
    #print(key, ":", diccionario2[key])
        for val in diccionario2[key]:
            print(diccionario2[key][i])
            i = i+1 #Aumenta en 1 el valor de i