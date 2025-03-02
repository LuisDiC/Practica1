import numpy as np
V = array


def bla(V,E):
    V=np.sort(V) #Vertices Ordenados
    E = np.array([]) #Numero de Aristas
    v1=np.array([V[0]])
    S=v1
    Vprima=v1
    Eprima=np.array([])
    Vdif=Buscar(V,Vprima)
    while(True):

        for x in S :

            for y in (Vdif):
                Vertice=np.array([x,y])
                for z in E:

                    if ((E[z]==Vertice).all()):

                        Vprima=np.concatenate(Vprima,y)
                        Eprima=np.concatenate(Eprima,Vertice)
                        Y=np.hstack(Y,y) # Me regresa los hijos

                Vdif=Buscar(V,Vprima)
            
        #if( V == False):
          
         # return T     
        
        S = Y

        Y = []

def Buscar(V,Vprima):
   i=np.searchsorted(V,Vprima)
   V=np.delete(V,i)
   return V
