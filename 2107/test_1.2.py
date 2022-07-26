"""Uso de la libreria JSON para tratar tipos de datos JSON"""

"""Importando la libreria JSON"""
import json

pythonDict = {"name": "Mary", "edad": 28, "dni": "2341434"}

"""Conversion de tipo de dato JSON: dumps()"""
dictToJson = json.dumps(pythonDict)
print("El dato convertido a JSON es el siguiente: {}".format(dictToJson))
print("El tipo de dato convertido es de tipo: {}".format(type(dictToJson)))
