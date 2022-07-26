"""Estructura de datos"""

"""Listas: hacer una copia de la lista original en otra"""

var1 = ["SQLServer", "RDS", "MySQL", "Postgresql"]

"""Usando Copy"""

var2 = var1.copy()

var2.append("SQLite3")
var2.remove("RDS")
print("Mi lista original es: {}".format(var1))
print("Mi copia de mi lista original es: {}".format(var2))
