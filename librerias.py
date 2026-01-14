import random

def generar_numeros_sorteo(cantidad, minimo=1, maximo=100):
    if cantidad > (maximo - minimo + 1):
        print("Error: La cantidad de números no puede exceder el rango.")
        return []
    
    numeros = random.sample(range(minimo, maximo + 1), cantidad)
    return sorted(numeros)

def main():
    print("=== GENERADOR DE NÚMEROS PARA SORTEO ===\n")
    
    try:
        cantidad = int(input("¿Cuántos números deseas? "))
        minimo = int(input("Número mínimo del rango: "))
        maximo = int(input("Número máximo del rango: "))
        
        numeros = generar_numeros_sorteo(cantidad, minimo, maximo)
        
        if numeros:
            print(f"\nNúmeros del sorteo: {numeros}")
    
    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")

main()