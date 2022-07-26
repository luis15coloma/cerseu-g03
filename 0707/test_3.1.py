"""Porgramación orientada a objetos"""

class Carro:
    """Atributos"""
    ruedas = 4


    """Constructor: valores que va a tener por defecto mi clase cuando se le instala a una variable"""
    def __int__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """Métodos: son las funciones de la clase"""
    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
        self.velocidad = velocidad
"""Instanciando en una variable mi Clase Carro"""
carro1 = Carro("azul", 40)
print("El color de mi carro es: {}".format(carro1.color))


