# Cuentas bancarias de un banco
class Cuenta:
    banco = "Santander"
    def __init__(self, titular, saldo):
        print(f"Creando cuenta de {titular}, con {saldo}€")

        self.titular = titular
        self.saldo = saldo

    # Definimos esta funcion para que a la hora de imprimir el objeto nos muestre los datos como queremos
    def __repr__(self):
        return f"Cuenta (Titular = '{self.titular}', Saldo = {self.saldo}, Banco = {self.banco})"

# Personal de un centro educativo
class Profesor:
    centro = "I.E.S Las Galletas"
    def __init__(self, dni, nombre, asignatura):
        print(f"\nCreando al profesor {nombre} con DNI {dni}, de la asignatura {asignatura}")

        self.dni = dni
        self.nombre = nombre
        self.asignatura = asignatura

    def __repr__(self):
        return f"Profesor (DNI = {self.dni}, Nombre = '{self.nombre}', Asignatura = {self.asignatura}, Centro = {self.centro})"

# Pacientes de un veterinario
class Ficha:
    def __init__(self, dueño, nombre_perro, raza):
        print(f"\nCreando al perro {nombre_perro}, de raza {raza}. Dueño: {dueño}")

        self.dueño = dueño
        self.nombre_perro = nombre_perro
        self.raza = raza

    def __repr__(self):
        return f"Ficha (Dueño = '{self.dueño}', Nombre_perro = {self.nombre_perro}, Raza = {self.raza})"
    
# Tipos de mascotas
class TipoMascota:
    def __init__(self, mascota, tipo):
        print(f"\nCreando a la mascota {mascota}, de tipo {tipo}.")

        self.mascota = mascota
        self.tipo = tipo

    def __repr__(self):
        return f"Tipo de Mascota (Mascota = '{self.mascota}', Tipo = {self.tipo})"

# Pruebas
nueva_cuenta = Cuenta("Jose", 10)
print(nueva_cuenta)

nuevo_profesor = Profesor("67487412P", "Jose", "Informática")
print(nuevo_profesor)

nueva_ficha = Ficha("Jose", "Max", "Golden Retriever")
print(nueva_ficha)

nuevo_tipoMascota = TipoMascota("Humano", "Mamífero")
print(nuevo_tipoMascota)



# Libros de una biblioteca
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __repr__(self):
        return f"Libro (Título = '{self.titulo}', Autor = '{self.autor}', ISBN = {self.isbn})"

# Gestión de biblioteca
class Biblioteca:
    def __init__(self, nombre):
        print(f"\nCreando biblioteca '{nombre}'")
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, titulo, autor, isbn):
        print(f"Agregando libro '{titulo}' a la biblioteca")
        libro = Libro(titulo, autor, isbn)
        self.libros.append(libro)
        return libro

    def quitar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                print(f"Removiendo libro '{libro.titulo}' de la biblioteca")
                self.libros.remove(libro)
        print(f"Libro con ISBN {isbn} no encontrado")

    def editar_libro(self, isbn, titulo=None, autor=None):
        for libro in self.libros:
            if libro.isbn == isbn:
                if titulo:
                    print(f"Editando título de '{libro.titulo}' a '{titulo}'")
                    libro.titulo = titulo
                if autor:
                    print(f"Editando autor a '{autor}'")
                    libro.autor = autor
                return libro
        print(f"Libro con ISBN {isbn} no encontrado")

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro

    def ver_lista(self):
        if not self.libros:
            print(f"La biblioteca '{self.nombre}' está vacía")
            return
        print(f"\nLibros en {self.nombre}:")
        for i, libro in enumerate(self.libros, 1):
            print(f"  {i}. {libro}")

    def __repr__(self):
        return f"Biblioteca (Nombre = '{self.nombre}', Total libros = {len(self.libros)})"

# Pruebas de Biblioteca
mi_biblioteca = Biblioteca("Biblioteca Municipal")
print(mi_biblioteca)

mi_biblioteca.agregar_libro("1984", "George Orwell", "978-0451524935")
mi_biblioteca.agregar_libro("El Quijote", "Miguel de Cervantes", "978-8408115595")
mi_biblioteca.agregar_libro("Cien años de soledad", "Gabriel García Márquez", "978-8401405735")
mi_biblioteca.ver_lista()

mi_biblioteca.editar_libro("978-0451524935", titulo="1984 - Edición Especial")
mi_biblioteca.ver_lista()

mi_biblioteca.quitar_libro("978-8408115595")
mi_biblioteca.ver_lista()