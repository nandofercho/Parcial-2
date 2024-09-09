class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}
        self.usuarios_registrados = set()

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro
        print("El libro ha sido añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print("El libro ha sido quitado de la biblioteca.")
        else:
            print("El libro con ISBN", isbn, "no está en la biblioteca.")

    def registrar_usuario(self, usuario):
        self.usuarios_registrados.add(usuario.user_id)
        print("Usuario registrado exitosamente.")

    def dar_de_baja_usuario(self, user_id):
        if user_id in self.usuarios_registrados:
            self.usuarios_registrados.remove(user_id)
            print("Usuario dado de baja exitosamente.")
        else:
            print("El usuario con ID", user_id, "no está registrado.")

    def prestar_libro(self, usuario, isbn):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles[isbn]
            if len(usuario.libros_prestados) < 3:  # máximo 3 libros prestados por usuario
                usuario.libros_prestados.append(libro)
                del self.libros_disponibles[isbn]
                print("El libro", libro.titulo_autor, "ha sido prestado a", usuario.nombre)
            else:
                print("El usuario ya ha alcanzado el límite máximo de libros prestados.")
        else:
            print("El libro con ISBN", isbn, "no está disponible.")

    def devolver_libro(self, usuario, isbn):
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro
                print("El libro", libro.titulo_autor, "ha sido devuelto.")
                return
        print("El usuario no tiene prestado el libro con ISBN", isbn)

    def buscar_libro(self, criterio, valor):
        resultados = []
        if criterio == "titulo":
            resultados = [libro for libro in self.libros_disponibles.values() if valor in libro.titulo_autor[0]]
        elif criterio == "autor":
            resultados = [libro for libro in self.libros_disponibles.values() if valor in libro.titulo_autor[1]]
        elif criterio == "categoria":
            resultados = [libro for libro in self.libros_disponibles.values() if valor == libro.categoria]
        elif criterio == "isbn":
            if valor in self.libros_disponibles:
                resultados = [self.libros_disponibles[valor]]
        return resultados

    def listar_libros_prestados(self, usuario):
        if usuario.libros_prestados:
            print("Libros prestados a", usuario.nombre + ":")
            for libro in usuario.libros_prestados:
                print("-", libro.titulo_autor)
        else:
            print(usuario.nombre, "no tiene libros prestados.")

    def guardar_datos(self, archivo_libros, archivo_usuarios):
        with open(archivo_libros, 'w') as f_libros:
            for libro in self.libros_disponibles.values():
                f_libros.write(f"{libro.titulo_autor[0]},{libro.titulo_autor[1]},{libro.categoria},{libro.isbn}\n")
        with open(archivo_usuarios, 'w') as f_usuarios:
            for user_id in self.usuarios_registrados:
                f_usuarios.write(f"{user_id}\n")

    def cargar_datos(self, archivo_libros, archivo_usuarios):
        with open(archivo_libros, 'r') as f_libros:
            for linea in f_libros:
                datos = linea.strip().split(',')
                libro = Libro(datos[0], datos[1], datos[2], datos[3])
                self.libros_disponibles[libro.isbn] = libro
        with open(archivo_usuarios, 'r') as f_usuarios:
            for linea in f_usuarios:
                user_id = linea.strip()
                self.usuarios_registrados.add(user_id)

# Función para ejecutar el sistema
def ejecutar_sistema():
    biblioteca = Biblioteca()
    while True:
        print("\nBienvenido al Sistema de Gestión de Biblioteca Digital")
        print("1. Añadir Libro")
        print("2. Quitar Libro")
        print("3. Ingresar Usuario")
        print("4. Dar de baja Usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libros")
        print("8. Lista de libros prestados")
        print("9. Guardar la biblioteca y usuario")
        print("10. Cargar la biblioteca y usuario")
        print("11. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            categoria = input("Ingrese la categoría del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            isbn = input("Ingrese el ISBN del libro que desea quitar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            nombre = input("Ingrese el nombre del usuario: ")
            user_id = input("Ingrese el ID del usuario: ")
            usuario = Usuario(nombre, user_id)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            user_id = input("Ingrese el ID del usuario que desea dar de baja: ")
            biblioteca.dar_de_baja_usuario(user_id)

        elif opcion == "5":
            user_id = input("Ingrese el ID del usuario: ")
            isbn = input("Ingrese el ISBN del libro que desea prestar: ")
            usuario = Usuario("", user_id)  # No se necesita el nombre para esta operación
            biblioteca.prestar_libro(usuario, isbn)

        elif opcion == "6":
            user_id = input("Ingrese el ID del usuario: ")
            isbn = input("Ingrese el ISBN del libro que desea devolver: ")
            usuario = Usuario("", user_id)  # No se necesita el nombre para esta operación
            biblioteca.devolver_libro(usuario, isbn)

        elif opcion == "7":
            criterio = input("Ingrese el criterio de búsqueda (titulo/autor/categoria/isbn): ")
            valor = input("Ingrese el valor de búsqueda: ")
            resultados = biblioteca.buscar_libro(criterio, valor)
            if resultados:
                print("Resultados de la búsqueda:")
                for libro in resultados:
                    print("Título:", libro.titulo_autor[0])
                    print("Autor:", libro.titulo_autor[1])
                    print("Categoría:", libro.categoria)
                    print("ISBN:", libro.isbn)
                    print("----------------------")
            else:
                print("No se encontraron libros con ese criterio de búsqueda.")

        elif opcion == "8":
            user_id = input("Ingrese el ID del usuario para ver sus libros prestados: ")
            usuario = Usuario("", user_id)  # No se necesita el nombre para esta operación
            biblioteca.listar_libros_prestados(usuario)

        elif opcion == "9":
            archivo_libros = input("Ingrese el nombre del archivo para guardar los libros: ")
            archivo_usuarios = input("Ingrese el nombre del archivo para guardar los usuarios: ")
            biblioteca.guardar_datos(archivo_libros, archivo_usuarios)
            print("Datos guardados exitosamente.")

        elif opcion == "10":
            archivo_libros = input("Ingrese el nombre del archivo con los libros: ")
            archivo_usuarios = input("Ingrese el nombre del archivo con los usuarios: ")
            biblioteca.cargar_datos(archivo_libros, archivo_usuarios)
            print("Datos cargados exitosamente.")

        elif opcion == "11":
            print("Gracias por usar el Sistema de Gestión de Biblioteca Digital. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

# Ejecutar el sistema
ejecutar_sistema()