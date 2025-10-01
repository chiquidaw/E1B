#Ejercicio 1
print(int(3.2+4))

#Ejercicio 2
x = 8
y = 6.2
print(x+y) 
print(x-y) 
print(x*y) 
print(x/y) 
print(x%y) 
print(x**y) 
print(x//y) 

#Ejercicio 3
a = 3
b = 8.2
c = None
d = "Hola Mundo!"
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Ejercicio 4
print("gor"*2+"ito") 
print("ca"*2+"túa") 

#Ejercicio 5
x = "ta"
y = "pa"
print(x+"ble"+x) 
print(y+y+"s") 

#Ejercicio 6
x = "Soy Juan y tengo"
y = 9
z = "años"
print(x,y,z)

#Ejercicio 7
producto = "pantalón"
precio = 40
rebaja = 20.5
print("El " + producto + " tiene un precio de " + str(precio) + "€ y con la rebaja del " + str(rebaja) + "% se queda en " + str(precio-(precio*(rebaja/100)))+"€")

#Ejercicio 8
x = 9
y = 9.5
print(x>y)

#Ejercicio 9
x = 7
y = 4.3
z = 2
print(x>y and x>z)

#Ejercicio 10
x = 2
if x % 2 == 0:
    print("x es un número par")
else:
    print("x no es un número par")