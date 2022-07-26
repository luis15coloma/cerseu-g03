"""Uso de la libreria de fechas y de tiempo"""

from datetime import datetime

strFecha = "2/6/2023"

conversion = datetime.strptime(strFecha, "%m/%d/%Y")
print("La fecha formateada es: {}".format(conversion))

"""Trae el me de la fecha con formato letras: strftime de datetime"""

conversionMes = datetime.strftime(conversion, "%b %d %Y")
print("Nuestra fecha con cambio en el mes es el siguiente: {}".format(conversionMes))
"""b: reemplaza a 'm'"""
