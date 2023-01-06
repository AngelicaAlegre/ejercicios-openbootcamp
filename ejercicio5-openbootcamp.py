def mifuncion():
    print("Nombre")
mifuncion()



def matematica(a, b):
    def suma(a, b):
        print(a + b)
    def resta(a, b):
        print(a - b)
    suma(a, b)
    resta(a, b)
matematica(5, 3)



def suma(a=1, b=10, c=8):
    print(a + b + c)
##Formas en las que puedo hacer correr mi codigo (todas son validas, algunas mas cortas que otras):
suma(1, 10, 8)
suma(a=5)
suma(a=1, b=10, c= 4)




def suma(*args):
    resultado = 0
    for arg in args:
        resultado += arg
    print(resultado)
suma(1, 2, 3, 4, 5, 0, 0, 0, 0)


def suma(**kwargs):
    print(kwargs)
suma(vivienda="piso", coche="rojo")


def suma(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)
suma(a="piso", b="rojo")


def suma(**kwargs):
    if kwargs ["coche"] == "bonito":
        print("Tu coche es bonito amigo")
suma(coche= "bonito")

def suma(**kwargs):
    if 'coche' in kwargs and kwargs['coche'] == 'bonito':
        print('Tu coche es bonito')
suma()


##NO UTILIZAR "PRINT" en la funcion solo RETURN:
def suma(a, b):
    return a + b
resultado = suma(4, 6)
print(resultado)