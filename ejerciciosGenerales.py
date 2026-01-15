import pandas as pd

import matplotlib.pyplot as plt

def diagrama_barras_notas(notas_dict, color):
    """
    Recibe un diccionario con notas de asignaturas y un color.
    Devuelve un diagrama de barras en el color especificado.
    """
    asignaturas = list(notas_dict.keys())
    notas = list(notas_dict.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(asignaturas, notas, color=color)
    plt.xlabel('Asignaturas')
    plt.ylabel('Notas')
    plt.title('Notas por Asignatura')
    plt.show()


def diagrama_cajas_notas(notas_serie):
    """
    Recibe una serie de Pandas con notas de alumnos.
    Devuelve un diagrama de cajas con título "Distribución de notas".
    """
    plt.figure(figsize=(8, 6))
    plt.boxplot(notas_serie)
    plt.ylabel('Notas')
    plt.title('Distribución de notas')
    plt.show()


def diagrama_ventas(ventas_serie, tipo_grafico):
    """
    Recibe una serie de Pandas con ventas por años y tipo de gráfico.
    Devuelve un diagrama del tipo indicado con título "Evolución del número de ventas".
    Tipos válidos: 'líneas', 'barras', 'sectores', 'áreas'.
    """
    plt.figure(figsize=(10, 6))
    
    if tipo_grafico == 'líneas':
        ventas_serie.plot(kind='line', marker='o')
    elif tipo_grafico == 'barras':
        ventas_serie.plot(kind='bar')
    elif tipo_grafico == 'sectores':
        ventas_serie.plot(kind='pie', autopct='%1.1f%%')
    elif tipo_grafico == 'áreas':
        ventas_serie.plot(kind='area')
    else:
        print("Tipo de gráfico no válido")
        return
    
    plt.xlabel('Años')
    plt.ylabel('Número de ventas')
    plt.title('Evolución del número de ventas')
    plt.tight_layout()
    plt.show()


# Ejemplos de uso
if __name__ == '__main__':
    # Ejemplo 1: Diagrama de barras de notas
    notas = {'Matemáticas': 8.5, 'Física': 7.2, 'Química': 9.1}
    diagrama_barras_notas(notas, 'blue')
    
    # Ejemplo 2: Diagrama de cajas
    notas_alumnos = pd.Series([7, 8, 6.5, 9, 7.5, 8.2, 6, 9.1])
    diagrama_cajas_notas(notas_alumnos)
    
    # Ejemplo 3: Diagrama de ventas
    ventas = pd.Series([100, 150, 200, 180, 250], index=['2020', '2021', '2022', '2023', '2024'])
    diagrama_ventas(ventas, 'líneas')