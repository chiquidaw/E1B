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

# Pruebas
nueva_cuenta = Cuenta("Jose", 10)
print(nueva_cuenta)

nuevo_profesor = Profesor("67487412P", "Jose", "Informática")
print(nuevo_profesor)

nueva_ficha = Ficha("Jose", "Max", "Golden Retriever")
print(nueva_ficha)