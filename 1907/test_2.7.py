"""Uso de la libreria datetime"""
"""Usando la función strptime"""

from datetime import datetime
print("La fecha actual es: {}".format(datetime.now()))

date = datetime.strptime("01/07/2022 20:20:00", "%d/%m/%Y %H:%M:%S")
print(date.strftime("%d de %m del %Y a las %H horas %M minutos y %S segundos"))