import pandas as pd
import numpy as np
grafo= pd.read_excel('dijikstra.xlsx', sheet_name='dijikstra',index_col=0)
grafo = grafo.fillna(0)
w = grafo
V=list(grafo.keys())
T = list(grafo.keys())
i=0
L={}
for x in T:
      L[x]=i
      i+=1
a = 'a'
z=V[-1]
grafo
for x in T: 
        L[x]=np.inf
L['a']=0
while z in T: 
    try:
        min_key = min(L, key=L.get) 
        v = T[T.index(min_key)]
        T.remove(v)
        for x in T:
            if (w[v][x]>0):
                L[x]=min(L[x],L[v]+w[v][x])
    except:
        L[min_key]=np.inf
        pass
print('La ruta con menor coste hacía z es: ', float(L['z']) )