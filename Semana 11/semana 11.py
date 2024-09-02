import json


class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado exitosamente.")
        else:
            print("El producto con ID {} no existe en el inventario.".format(id))

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
            print("Producto actualizado exitosamente.")
        else:
            print("El producto con ID {} no existe en el inventario.".format(id))

    def buscar_producto_por_nombre(self, nombre):
        encontrados = []
        for producto in self.productos.values():
            if producto.nombre.lower() == nombre.lower():
                encontrados.append(producto)
        return encontrados

    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            productos_serializados = [vars(producto) for producto in self.productos.values()]
            json.dump(productos_serializados, archivo, indent=4)
        print("Inventario guardado exitosamente en el archivo {}.".format(nombre_archivo))

    def cargar_inventario(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                productos_serializados = json.load(archivo)
                for producto_serializado in productos_serializados:
                    producto = Producto(**producto_serializado)
                    self.agregar_producto(producto)
            print("Inventario cargado exitosamente desde el archivo {}.".format(nombre_archivo))
        except FileNotFoundError:
            print("El archivo {} no existe. No se pudo cargar el inventario.".format(nombre_archivo))


def mostrar_menu():
    print("\n=== Menú ===")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar inventario")
    print("6. Guardar inventario en archivo")
    print("7. Cargar inventario desde archivo")
    print("8. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            id = input("Ingrese el ID del producto que desea eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == "3":
            id = input("Ingrese el ID del producto que desea actualizar: ")
            cantidad = input("Ingrese la nueva cantidad del producto (deje en blanco para mantener la actual): ")
            precio = input("Ingrese el nuevo precio del producto (deje en blanco para mantener el actual): ")
            if cantidad:
                cantidad = int(cantidad)
            if precio:
                precio = float(precio)
            inventario.actualizar_producto(id, cantidad, precio)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto que desea buscar: ")
            productos_encontrados = inventario.buscar_producto_por_nombre(nombre)
            if productos_encontrados:
                print("Productos encontrados:")
                for producto in productos_encontrados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")
        elif opcion == "5":
            print("=== Inventario ===")
            inventario.mostrar_inventario()
        elif opcion == "6":
            nombre_archivo = input("Ingrese el nombre del archivo para guardar el inventario: ")
            inventario.guardar_inventario(nombre_archivo)
        elif opcion == "7":
            nombre_archivo = input("Ingrese el nombre del archivo para cargar el inventario: ")
            inventario.cargar_inventario(nombre_archivo)
        elif opcion == "8":
            print("Gracias por utilizar el Sistema Avanzado de Gestión de Inventario")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()