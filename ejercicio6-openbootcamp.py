class Color:
    color = "Negro"
class Ruedas:
    cantidad = 4
class Puertas:
    cantidad = 5
class Velocidad:
    velocidad = "60km/h"
class Cilindradas:
    cilindradas = 3

class Vehiculo:
    puertas = Puertas()
    color = Color()
    ruedas = Ruedas()

class Coche(Vehiculo):
    velocidad = Velocidad()
    cilindradas = Cilindradas()

toyota = Coche()
print(toyota.puertas.cantidad)
print("El coche es de color", toyota.color)
print("Cuenta con", toyota.ruedas.cantidad, "ruedas")








#class Vehiculo:
#     def __init__(self, color, ruedas, puertas):
#         self.color = color
#         self.ruedas = ruedas
#         self.puertas = puertas


# class Coche(Vehiculo):
#     def __init__(self, velocidad, cilindradas, color, ruedas, puertas):
#         self.velocidad = velocidad
#         self.cilindradas = cilindradas
#         Vehiculo.__init__(self, color, ruedas, puertas)
# toyota = Coche(60, 2, "Negro", 4, 6)
# print("Mi coche es de color", toyota.color)

# class Color:
#     color = "Negro"
# class Ruedas:
#     cantidad = 4
# class Puertas:
#     cantidad = 5
# class Cilindradas:
#     cilindradas = 2

# class Coche(Vehiculo):
#     velocidad = Velocidad()
#     cilindradas = Cilindradas()
# class Velocidad:
#     velocidad = "60km/h"

# c = Coche()
# print("El vehiculo es de color", c.vehiculo.color)
# print("Su velocidad minima es de", c.coche.velocidad)