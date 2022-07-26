"""Uso de la libreria de fechas y de tiempo"""
"""Conversión total del tiempo"""

from datetime import datetime

timeNow = datetime.strptime("2023/02/01 20:40:00", "%Y/%m/%d %H:%M:%S").timestamp()
print("La conversión de nuestro tiempo es: {}".format(timeNow))
