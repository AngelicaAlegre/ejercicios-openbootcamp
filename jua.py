class Vehiculo:
    nombre = ""
    precio = 0.0
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def getNombre(self):
        return self.nombre
vehiculo = Vehiculo("Mercedes", "200.000")
# print(Vehiculo.getNombre())


f = open('./fichero.txt', 'a+')
f.write('Este vehiculo vale: ' + vehiculo.precio + ' y es un: ' + vehiculo.nombre)
f.close()