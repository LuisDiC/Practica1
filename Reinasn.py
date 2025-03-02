def es_seguro(tablero, fila, col):
    for i in range(fila):
        #print(col)
        if tablero[i] == col or \
           tablero[i] - i == col - fila or \
           tablero[i] + i == col + fila:
            return False
    return True

def resolver_reinas(n):
    def colocar_reinas(fila):
        if fila == n:
            soluciones.append(tablero[:])
            return
        for col in range(n):
            if es_seguro(tablero, fila, col):
               # print(tablero)
                tablero[fila] = col
                colocar_reinas(fila + 1)

    soluciones = []
    tablero = [-1] * n
    colocar_reinas(0)
    return soluciones

soluciones = resolver_reinas(9)
for sol in soluciones:
    print(sol)