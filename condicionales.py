#Ejercicio 1
contador = 30
while contador <= 50 :
    print(contador)
    contador += 1

#Ejercicio 2
edad = int(input("Introduce tu edad: "))
ingresos = int(input("Introduce tus ingresos mensuales: "))

if (edad > 16 and ingresos >= 1000) :
    print("Tienes que tributar :(")
else : 
    print("No tienes que tributar :)")

#Ejercicio 3
nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (M para mujer, H para hombre): ")

primera_letra = nombre[0] 
grupo = ""

if (sexo == "M" and primera_letra < "M") or (sexo == "H" and primera_letra > "N"):
    grupo = "A"
else :
    grupo = "B"

print("Tu grupo es: " + grupo)

#Ejercicio 4
puntuacion = float(input("Introduce tu puntuación (EJ: 0.0, 0.4, 0.6 o más): "))
nivel = ""
dinero = 0.0

# Determinamos el nivel y el dinero
if puntuacion == 0.0:
    nivel = "Inaceptable"
    dinero = 2400 * puntuacion
elif puntuacion == 0.4:
    nivel = "Aceptable"
    dinero = 2400 * puntuacion
elif puntuacion >= 0.6:
    nivel = "Meritorio"
    dinero = 2400 * puntuacion
else:
    nivel = "Puntuación no válida"
    dinero = 0.0

# Mostramos el resultado
print("Nivel de rendimiento: " + nivel)
print("Cantidad de dinero: " + str(dinero) + "€")

#Ejercicio 5

