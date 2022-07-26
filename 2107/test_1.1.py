"""Uso de la libreria JSON para tratar tipos de datos JSON"""

"""Importando la libreria JSON"""

import json
"""Creando nuestra variable con un tipo de dato JSON"""
jsonData = '{"nombre": "Python", "tipo": "Backend", "paradigma": "POO"}'

"""Convertiendo a un dato que pueda manejar Python: loads()"""

jsonToPython = json.loads(jsonData)

print("Nuestro dato de tiepo JSON a dato para Python: {}".format(jsonToPython))

print(jsonToPython['paradigma'])

print("El tipo de dato de nuestra variable es: {}".format(type(jsonToPython)))
