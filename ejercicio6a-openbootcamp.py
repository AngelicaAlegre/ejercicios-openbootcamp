class Alumno:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def resultado(self):
        if self.nota > 6:
            print("Aprobó el examen")
        else:
            print("No aprobó el examen")

Alumno1 = Alumno()
Alumno2 = Alumno()
Alumno1.inicializar("Juan Mendez", 8)
Alumno2.inicializar("Yesi Rodriguez", 10)
Alumno1.imprimir()
Alumno1.resultado()
Alumno2.imprimir()
Alumno2.resultado()



class Persona:
    Nombre: "Juan"
    Edad = 23
    Residencia = "Posadas"
print(dir(Persona))
