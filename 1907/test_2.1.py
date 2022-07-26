"""Uso de la libreria de fechas y tiempos"""

from datetime import date, time, datetime

fecha = date.today()
print("La fecha a manejar es la siguiente: {}".format(fecha))


tiempo = datetime.now()
print("El tiempo actual es: {}".format(tiempo))

año = tiempo.year
mes = tiempo.month
dia = tiempo.day

print("Año actual es: {}".format(año))
print("Mes actual es: {}".format(mes))
print("Día actual es: {}".format(dia))

"""Uso del datetime para extraer la hora, minuto y segundo"""
hora = tiempo.hour
minuto = tiempo.minute
segundo = tiempo.second

print("La hora exacta son las {} horas, {} minutos y {} segundos".format(hora, minuto, segundo))
