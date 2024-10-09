### 09-10-2024 ###

class ProgramaTres: #Se coloca el nombre del programa (nombre físico) para la clase principal

    def __init__(self):
        self.unidadUno = [98, 58, 78, 65, 12]
        self.unidadDos = [87, 68, 98, 89, 100]
        self.unidadTres = [56, 54, 79, 85, 84]
        self.nombres = ["Luis", "Jorge", "Sebastian", "Carlos", "Iván"]
        self.prom = []

    def promedio(self):
        for i in range(len(self.unidadUno)):
            suma = (self.unidadUno[i] + self.unidadDos[i] + self.unidadTres[i]) / 3
            self.prom.append(suma)

    def maxPromedio(self):
        valormax = max(self.prom)
        indice = self.prom.index(valormax)
        print(f"El alumno con el promedio más alto: {self.nombres[indice]} con un promedio de: {valormax}")

    def imprimirArreglos(self):
        for i in range(len(self.nombres)):
            print(f"{self.nombres[i]} - {self.unidadUno[i]} - {self.unidadDos[i]} - {self.unidadTres[i]} - {self.prom[i]}")

    def minPromedio(self):
        valormin = min(self.prom)
        indice = self.prom.index(valormin)
        print(f"El alumno con el promedio más bajo: {self.nombres[indice]} con un promedio de: {valormin}")

    def pedirNombre(self):
        buscar = input("Escribe el nombre la persona a buscar: ")
        for i in range(len(self.nombres)):
            if self.nombres[i] == buscar:
                print(f"{self.nombres[i]} - {self.unidadUno[i]} - {self.unidadDos[i]} - {self.unidadTres[i]} - {self.prom[i]}")

    def minCalificacion(self):
        vn = []
        vn.append(min(self.unidadUno))
        vn.append(min(self.unidadDos))
        vn.append(min(self.unidadTres))
        print(f"La calificación menor de la tres unidades es: {min(vn)}")

    def maxCalificacion(self):
        vn = []
        vn.append(max(self.unidadUno))
        vn.append(max(self.unidadDos))
        vn.append(max(self.unidadTres))
        print(f"La calificación menor de la tres unidades es: {max(vn)}")



of = ProgramaTres()
of.promedio()
#of.maxPromedio()
#of.minPromedio()
#of.pedirNombre()
#of.imprimirArreglos()
of.minCalificacion()
of.maxCalificacion()


#Si tiene una unidad menor de 60, está reprobado (NA)