"""Ejercicio N°4 de Clases en python
4. Crear un programa el cual pueda declarar dos valores enteros
Reglas:
- El banco va a requerir que al finalizar el día calcule el dinero depositado
- Crear dos clases, una clase cliente y otra clase banco
- La clase cliente tendrás los atributos de nombre y cantidad
- Crear los métodos constructor, depositar, extraer, mostrar el total de dinero depositado
- El banco tendrá 3 atributos de la clase cliente, el método cosntructor, operar y deposito total
- Instanciar para el caso de 3 personas
- Mostrar los datos de todos los clientes, incluyendo el monto total de cada uno
"""

class Banco():

    def __init__(self):
        self.cliente1 = Cliente("Susana")
        self.cliente2 = Cliente("Jorge")
        self.cliente3 = Cliente("Elizabeth")

    def operar(self):
        self.cliente1.depositar(500)
        self.cliente2.depositar(1000)
        self.cliente3.depositar(80)
        self.cliente1.extraer(40)

    def deposito(self):
        total = self.cliente1.mostrarCantidad() + self.cliente2.mostrarCantidad() + self.cliente3.mostrarCantidad()
        print("El total de diner que tiene el banco es: {}".format(total))
        self.cliente1.imprimirDatos()
        self.cliente2.imprimirDatos()
        self.cliente3.imprimirDatos()

class Cliente():

    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0

    def depositar(self, monto):
        self.cantidad += monto

    def extraer(self, monto):
        self.cantidad -= monto

    def mostrarCantidad(self):
        return self.cantidad

    def imprimirDatos(self):
        print("{} tiene la cantidad depositada de {}".format(self.nombre, self.cantidad))

banco = Banco()
banco.operar()
banco.deposito()

banco.cliente1.imprimirDatos()