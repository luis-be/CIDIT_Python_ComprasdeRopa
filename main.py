class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Cantidad: {self.cantidad}")

    def comprar(self, cantidad_a_comprar):
        if cantidad_a_comprar > self.cantidad:
            print("No hay suficiente cantidad disponible.")
        else:
            self.cantidad -= cantidad_a_comprar
            print(f"Has comprado {cantidad_a_comprar} unidades de {self.nombre}.")


class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre,precio,cantidad)
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Cantidad: {self.cantidad}, Talla: {self.talla}")

class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre,precio,cantidad)
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Cantidad: {self.cantidad}, Talla: {self.talla}")

class Inventario:
    def __init__(self):
        self.prendas = [] 

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda) 

    def mostrar_inventario(self):

        print("Inventario de Prendas:")
        for prenda in self.prendas:
            prenda.mostrar_info()  


def menu():
    inventario = Inventario()
    while True:
        print("\nMenu:")
        print("1. Añadir prenda")
        print("2. Ver inventario")
        print("3. Comprar prenda")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            while True:
                print("\nMenu:")
                print("1. Añadir prenda de Hombre")
                print("2. Añadir prenda de Mujer")
                print("3. Volver al menu principal")

                opcion = input("Selecciona una opción: ")

                if opcion == '1':
                    while True:
                        nombre = input("Nombre de la prenda: ")
                        precio = float(input("Precio: "))
                        cantidad = int(input("Cantidad: "))
                        talla = input("Talla: ")
                        ropa_hombre = RopaHombre(nombre, precio, cantidad, talla)
                        inventario.agregar_prenda(ropa_hombre)
                        break
                if opcion == '2':
                    while True:
                        nombre = input("Nombre de la prenda: ")
                        precio = float(input("Precio: "))
                        cantidad = int(input("Cantidad: "))
                        talla = input("Talla: ")
                        ropa_mujer = RopaMujer(nombre, precio, cantidad, talla)
                        inventario.agregar_prenda(ropa_mujer)
                        break
                if opcion == '3':
                        break
                else:
                    print("Introduce una opción válida")

        elif opcion == '2':
            inventario.mostrar_inventario()

        elif opcion == '3':
            inventario.mostrar_inventario()
            nombre = input("Introduce el nombre de la prenda que deseas comprar: ")
            cantidad = int(input("¿Cuántas unidades deseas comprar?: "))
            for prenda in inventario.prendas:
                if prenda.nombre == nombre:
                    prenda.comprar(cantidad)
                    break
            else:
                print("Prenda no encontrada.")
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, por favor selecciona otra.")

menu()