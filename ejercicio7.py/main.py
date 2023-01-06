import operaciones

# Cuando trabajamos con modulos de archivos, el principal siempre es "main" o "index"
# carpeta === paquete
# archivo === modulo

def ejercicio():
    res = operaciones.suma(4, 2)
    resResta = operaciones.resta(8, 3)
    resDivision = operaciones.division(10, 5)
    resMultiplicacion = operaciones.multiplicacion(2, 2)
    print('Resultado de ejercicio:', res)

if __name__ == '__main__':
    ejercicio()






import time

hora = time.strftime('%H') 
minutos = time.strftime('%M') 

if int(hora) >= 19:
	print ("Es hora de irse a casa") 
else:
	print ("Quedan {} horas y {} minutos para irnos a casa".format(18- int(hora), 59-int(minutos)))