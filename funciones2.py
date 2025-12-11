# 1.1 - Pasar de decimal a binario
def decimal_binario(n):
    if n == 0:
        return "0"
    binario = ""
    while n > 0:
        residuo = n % 2
        binario = str(residuo) + binario # Añade el resto al principio
        n = n // 2 # División entera
    return binario

numeroDecimal = 5
print("Numero de decimal a binario (", numeroDecimal, "): ", decimal_binario(numeroDecimal))

# 1.2 - Pasar de binario a decimal
def binario_decimal(x):
    return int(x, 2) # Al colocarlo en base 2, el lenguaje entiende que lo devuelva en decimal

numeroBinario = decimal_binario(numeroDecimal)
print("Numero de binario a decimal (", numeroBinario, "): ", binario_decimal(numeroBinario))

# 2 - Diccionario con media, varianza y desviación típica

def estadisticas(muestra):
    n = len(muestra)
    media = sum(muestra) / n
    
    varianza = sum((x * 1.0 - media) ** 2 for x in muestra) / n
    desviacion_tipica = varianza ** 0.5

    return {
        "media": media,
        "varianza": varianza,
        "desviacion_tipica": desviacion_tipica
    }

datos = [1, 2, 3, 4, 5]
print(estadisticas(datos))
