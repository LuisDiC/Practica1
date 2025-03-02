import pandas as pd
grafo = pd.read_excel('grafos.xlsx', sheet_name='grafo1', index_col=0)
grafo = grafo.fillna(0)
V = list(grafo.columns)
def bll(V):
    v1 = 'a'  # Nodo inicial
    Vp = [v1]  # Lista de nodos visitados
    Ep = []  # Lista de aristas del árbol de expansión
    w = v1  # Nodo actual
    stack = [w]  # Pila para la búsqueda en profundidad

    while stack:
        stack.pop()
        for v in V:
            if grafo[w][v] > 0 and v not in Vp:
                Ep.append((w, v))
                Vp.append(v)
                stack.append(v)
                w=v
                break
    T = [Ep,Vp]
            
    print(T)
    
bll(V)
