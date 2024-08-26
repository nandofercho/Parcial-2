# Definición de la clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio


# Definición de la clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    # Método para añadir un nuevo producto al inventario
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Método para eliminar un producto por su ID
    def eliminar_producto(self, id):
        self.productos = [p for p in self.productos if p.get_id() != id]

    # Método para actualizar cantidad o precio de un producto por su ID
    def actualizar_producto(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                break

    # Método para buscar productos por nombre
    def buscar_producto_por_nombre(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    # Método para mostrar todos los productos en el inventario
    def mostrar_productos(self):
        for p in self.productos:
            print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")

    # Método para guardar el inventario en un archivo de texto
    def guardar_inventario(self, filename):
        with open(filename, 'w') as file:
            for p in self.productos:
                file.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")

    # Método para cargar el inventario desde un archivo de texto
    def cargar_inventario(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                id, nombre, cantidad, precio = line.strip().split(',')
                producto = Producto(id, nombre, int(cantidad), float(precio))
                self.agregar_producto(producto)


# Función para mostrar el menú y manejar la interfaz de usuario
def mostrar_menu():
    print("\n=== Menú ===")
    print("1. Agregar nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto por ID")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Guardar inventario en archivo")
    print("7. Cargar inventario desde archivo")
    print("8. Salir")


# Función principal
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
            print("Producto agregado correctamente.")
        elif opcion == "2":
            id = input("Ingrese el ID del producto que desea eliminar: ")
            inventario.eliminar_producto(id)
            print("Producto eliminado correctamente.")
        elif opcion == "3":
            id = input("Ingrese el ID del producto que desea actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco si no desea actualizar): ")
            precio = input("Ingrese el nuevo precio (deje en blanco si no desea actualizar): ")
            inventario.actualizar_producto(id, cantidad=int(cantidad) if cantidad else None,
                                           precio=float(precio) if precio else None)
            print("Producto actualizado correctamente.")
        elif opcion == "4":
            nombre = input("Ingrese el nombre (o parte del nombre) del producto que desea buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre)
            if resultados:
                print("Resultados de la búsqueda:")
                for producto in resultados:
                    print(
                        f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
            else:
                print("No se encontraron productos con ese nombre.")
        elif opcion == "5":
            print("Lista de productos en el inventario:")
            inventario.mostrar_productos()
        elif opcion == "6":
            filename = input("Ingrese el nombre del archivo para guardar el inventario: ")
            inventario.guardar_inventario(filename)
            print("Inventario guardado correctamente.")
        elif opcion == "7":
            filename = input("Ingrese el nombre del archivo para cargar el inventario: ")
            inventario.cargar_inventario(filename)
            print("Inventario cargado correctamente.")
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()