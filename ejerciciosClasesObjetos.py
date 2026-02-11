# ==============================
# EJERCICIO 1
# ==============================

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def get_max_speed(self):
        return self.max_speed

    def increase_mileage(self, amount_to_increase):
        self.mileage += amount_to_increase


# ==============================
# EJERCICIO 2
# ==============================

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print("Longitud:", self.length)
        print("Anchura:", self.width)
        print("Perímetro:", self.perimeter())
        print("Área:", self.area())

    def __str__(self):
        return f"Rectángulo -> Longitud: {self.length}, Anchura: {self.width}, Perímetro: {self.perimeter()}, Área: {self.area()}"


# ==============================
# EJERCICIO 3
# ==============================

class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

    def transfer(self, other_account, amount):
        self.withdrawal(amount)
        other_account.deposit(amount)

    def apply_bank_fees(self, percentage):
        self.balance -= self.balance * (percentage / 100)

    def display(self):
        print("Número de cuenta:", self.account_number)
        print("Titular:", self.name)
        print("Saldo:", self.balance)

    # Comparar cuentas por saldo
    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance


# ==============================
# EJERCICIO 4
# ==============================

class Vehicle2:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle2):
    def fare(self):
        total = super().fare()
        return total + total * 0.10


# ==============================
# PROGRAMA PRINCIPAL
# ==============================

def main():

    # Ejercicio 1
    print("EJERCICIO 1")
    car = Vehicle(200, 15000)
    print("Velocidad máxima:", car.get_max_speed())
    car.increase_mileage(500)
    print("Nuevo kilometraje:", car.mileage)

    # Ejercicio 2
    print("\nEJERCICIO 2")
    rect = Rectangle(10, 5)
    rect.display()
    print(rect)

    # Ejercicio 3
    print("\nEJERCICIO 3")
    cuenta1 = BankAccount(1, "Ana", 1000)
    cuenta2 = BankAccount(2, "Luis", 500)

    cuenta1.transfer(cuenta2, 200)
    cuenta1.apply_bank_fees(5)

    cuenta1.display()
    print()
    cuenta2.display()

    print("¿Cuenta1 tiene más saldo que Cuenta2?", cuenta1 > cuenta2)

    # Ejercicio 4
    print("\nEJERCICIO 4")
    School_bus = Bus("School Volvo", 12, 50)
    print("Total Bus fare is:", School_bus.fare())


if __name__ == "__main__":
    main()