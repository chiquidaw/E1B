#Ejercicio 1
entero = 42
flotante = 3.14
cadena = "Hola"
booleano = True

print(type(entero))
print(type(flotante))
print(type(cadena))
print(type(booleano))

#Ejercicio 2
numero_str = "123"
como_entero = int(numero_str)
como_flotante = float(numero_str)

print(como_entero, type(como_entero))
print(como_flotante, type(como_flotante))

#Ejercicio 3
nombre = input("Introduce tu nombre: ")
edad_str = input("Introduce tu edad: ")
edad = int(edad_str)
print(f"Hola {nombre}, tienes {edad} años.")

#Ejercicio 4
a = 5
b = 2.5
suma = a + b
print(suma)
print(type(suma))

#Ejercicio 5
comparacion = 10 > 5
print(comparacion)
print(type(comparacion))

#Ejercicio 6
x = 12
y = 5
print("suma", x + y)
print("resta", x - y)
print("producto", x * y)
print("division", x / y)
print("division entera", x // y)
print("modulo", x % y)
print("potencia", x ** y)

#Ejercicio 7
a = 7
b = 10
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

#Ejercicio 8
v1 = True
v2 = False
print("v1 and v2 ->", v1 and v2)
print("v1 or v2 ->", v1 or v2)
print("not v1 ->", not v1)
print("not v2 ->", not v2)

#Ejercicio 9
x = 10
x += 5
print("x despues de += 5:", x)
x -= 3
print("x despues de -= 3:", x)
x *= 2
print("x despues de *= 2:", x)
x /= 4
print("x despues de /= 4:", x)

#Ejercicio 10
s1 = "Hola "
s2 = "mundo"
concatenada = s1 + s2
print(concatenada)
repetida = s2 * 3
print(repetida)

#Ejercicio 11
a_str = input("Introduce el primer número: ")
b_str = input("Introduce el segundo número: ")
a = float(a_str)
b = float(b_str)

print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
if b != 0:
    print(f"División: {a / b}")
else:
    print("División: Error - división por cero")
