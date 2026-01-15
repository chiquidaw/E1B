from collections import deque

def construir_laberinto(dimensiones, muros):
    """Construye el laberinto a partir de las coordenadas de los muros"""
    filas, columnas = dimensiones
    laberinto = [[' ' for _ in range(columnas)] for _ in range(filas)]
    
    for fila, columna in muros:
        laberinto[fila][columna] = 'X'
    
    laberinto[filas - 1][columnas - 1] = 'S'  # Marca la salida
    return laberinto


def resolver_laberinto(laberinto):
    """Resuelve el laberinto y devuelve la secuencia de movimientos"""
    
    filas = len(laberinto)
    columnas = len(laberinto[0])
    inicio = (0, 0)
    salida = (filas - 1, columnas - 1)
    
    # Direcciones: Arriba, Abajo, Izquierda, Derecha
    direcciones = [(-1, 0, 'Arriba'), (1, 0, 'Abajo'), (0, -1, 'Izquierda'), (0, 1, 'Derecha')]
    
    cola = deque([(inicio, [])])
    visitados = {inicio}
    
    while cola:
        (fila, columna), camino = cola.popleft()
        
        if (fila, columna) == salida:
            return camino
        
        for df, dc, direccion in direcciones:
            nueva_fila, nueva_columna = fila + df, columna + dc
            
            if (0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and
                laberinto[nueva_fila][nueva_columna] != 'X' and
                (nueva_fila, nueva_columna) not in visitados):
                
                visitados.add((nueva_fila, nueva_columna))
                cola.append(((nueva_fila, nueva_columna), camino + [direccion]))
    
    return []  # No hay solución


# Ejemplo de uso
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
laberinto = construir_laberinto((5, 5), muro)

# Mostrar laberinto
for fila in laberinto:
    print(''.join(fila))

# Resolver
movimientos = resolver_laberinto(laberinto)
print("\nMovimientos:", movimientos)