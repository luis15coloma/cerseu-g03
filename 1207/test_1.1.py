"""
1. Realizar un programa que cotnenga una clase llamada alumno

Reglas:
- Debe tener los atributos de nombre y la nota para el alumno
- Definir los métodos para inicializar sus atribuciones, imprimirlos y mostrar un mensaje con el resultado de la nota
- Mostrar en el mensaje si el alumno aprobó o no
"""

class Alumno:
    "Inicializar los atributos"
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    """Método para imprimir los datos"""
    def resultado(self):
