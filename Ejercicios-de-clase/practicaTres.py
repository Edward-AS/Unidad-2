### 11-10-2024 ###

"""
--> Son un total de cinco produtos

Clave = [666]
Nombre = [Arroz]
Costo = [16.50] -> Se vende al precio del costo más el 10%
Existencia = [1] -> Inventario
Venta = [2] -> Número de ventas realizadas del producto
Ganancia = [2.70] -> Ganancia monetaria

Si la existencia es igual a cero, entonces no se puede realizar la venta

Si extiste, cuántos quiere comprar; sino, entonces informar que no se puede realizar la venta

---> Qué producto desea comprar
---> Qué producto se vendió más
---> Qué producto se vendió menos
---> Cuál se tiene más
---> Cuál se tiene menos
"""

from os import system

class Tienda:

    def __init__(self):
        self.clave = [253, 789, 320, 439, 462]
        self.nombre = ["Cereal", "Huevo", "Arroz", "Leche", "Chocolate"]
        self.costo = [56, 75, 23, 40, 15]
        self.existencia = [90, 60, 129, 32, 5]
        self.venta = [0, 0, 0, 0, 0]
        self.ganancia = [0, 0, 0, 0, 0]

    def mas_producto(self):
        mayor_cantidad = max(self.existencia)
        indice = self.existencia.index(mayor_cantidad)
        print(f"\nEl producto con mayor existencia en stock: {self.nombre[indice]} Clave: {self.clave[indice]}\n\t Cantidad: {mayor_cantidad}")

    def menor_producto(self):
        menor_cantidad = min(self.existencia)
        indice = self.existencia.index(menor_cantidad)
        print(f"\nEl producto con menor existencia en stock: {self.nombre[indice]} Clave: {self.clave[indice]}\n\t Cantidad: {menor_cantidad}")

    def mas_vendido(self):
        mayor_vendido = max(self.venta)
        indice = self.venta.index(mayor_vendido)
        print(f"\nEl producto más vendido es: {self.nombre[indice]} Clave: {self.clave[indice]}\n\t Cantidad: {mayor_vendido}")
    
    def menor_vendido(self):
        menor_vendido = min(self.venta)
        indice = self.venta.index(menor_vendido)
        print(f"\nEl producto menos vendido es: {self.nombre[indice]} Clave: {self.clave[indice]}\n\t Cantidad: {menor_vendido}")

    def vender(self):
        for i in range(len(self.clave)):
            print(f"{i + 1}.- {self.nombre[i]}\n -- Clave: {self.clave[i]} -- ${self.costo[i]}\n -- Existencia: {self.existencia[i]}\n")
        clav = int(input("Ingrese la clave del producto que desea comprar: "))
        if not clav in self.clave:
            print("\nLa clave no es válida\n\tSaliendo...")
        else:
            ind = self.clave.index(clav)
            if self.existencia[ind] == 0:
                print("\nNo existen productos en stock\n\tSaliendo...")
            else:
                cantidad = int(input("Ingrese el número de productos que desea comprar: "))
                if cantidad > self.existencia[ind]:
                    print("No hay suficiente stock")
                else:
                    self.existencia[ind] -= cantidad
                    self.venta[ind] = cantidad
                    ganancia = (self.costo[ind] + (self.costo[ind] * 0.1)) * cantidad
                    self.ganancia[ind] = ganancia
                    print(f"\n--> Cuenta:\n{self.nombre[ind]} --- ${ganancia}")

    def menu(self):
        while True:
            system("cls") 
            print("\n******MENÚ******")
            print("1) Realizar compra")
            print("2) El producto más vendido")
            print("3) El producto menos vendido")
            print("4) Producto con mayor existencia")
            print("5) Producto con menor existencia")
            print("6) Salir")
            opc = int(input("Seleccione una opción: "))
            match opc:
                case 1:
                    self.vender()
                case 2:
                    self.mas_vendido()
                case 3:
                    self.menor_vendido()
                case 4:
                    self.mas_producto()
                case 5:
                    self.menor_producto()
                case 6:
                    print("\n\tSaliendo...")
                    break
                case _:
                    print("Opción no válida")
            input()

x = Tienda()
x.menu()