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

print("Nivel de rendimiento: " + nivel)
print("Cantidad de dinero: " + str(dinero) + "€")

#Ejercicio 5
print("Tipos de pizza disponibles:")
print("1. Vegetariana")
print("2. No vegetariana")

opcion = input("¿Quieres una pizza vegetariana (1) o no vegetariana (2)? ")

ingredientes_base = ["Mozzarella", "Tomate"]

if opcion == "1":
    print("\nHas elegido una pizza vegetariana.")
    print("Ingredientes disponibles:")
    print("1. Pimiento")
    print("2. Tofu")
    
    ingrediente = input("Elige un ingrediente (1-2): ")
    if ingrediente == "1":
        ingrediente_elegido = "Pimiento"
    elif ingrediente == "2":
        ingrediente_elegido = "Tofu"
    else:
        print("Opción no válida. Se elegirá Pimiento por defecto.")
        ingrediente_elegido = "Pimiento"
    
    ingredientes_base.append(ingrediente_elegido)
    print("\nTu pizza es VEGETARIANA con los siguientes ingredientes:", ", ".join(ingredientes_base))

elif opcion == "2":
    print("\nHas elegido una pizza no vegetariana.")
    print("Ingredientes disponibles:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")
    
    ingrediente = input("Elige un ingrediente (1-3): ")
    if ingrediente == "1":
        ingrediente_elegido = "Peperoni"
    elif ingrediente == "2":
        ingrediente_elegido = "Jamón"
    elif ingrediente == "3":
        ingrediente_elegido = "Salmón"
    else:
        print("Opción no válida. Se elegirá Peperoni por defecto.")
        ingrediente_elegido = "Peperoni"
    
    ingredientes_base.append(ingrediente_elegido)
    print("\nTu pizza es NO VEGETARIANA con los siguientes ingredientes:", ", ".join(ingredientes_base))

else:
    print("\nOpción incorrecta. Inténtalo de nuevo.")

