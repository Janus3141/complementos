#! /usr/bin/python

# 5ta Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos


import pqueue
import unionfind


def prim(grafo):
    '''
    Dado un grafo (en formato de listas con pesos), aplica el algoritmo de Prim
    y retorna el MST correspondiente. 
    NOTA: El grafo de entrada se asume conexo.
    '''
    nodos, aristas = grafo
    queue = pqueue.pqueue()
    for a in aristas:
        queue.add(a, a[2])
    nodos_arbol = set()
    aristas_arbol = list()
    while queue.size != 0:
        arista, peso = queue.pop()
        if arista[0] in nodos_arbol and arista[1] in nodos_arbol:
            continue
        else:
            nodos_arbol.add(arista[0])
            nodos_arbol.add(arista[1])
            aristas_arbol.append(arista)
    return [nodos[:], aristas_arbol]


def kruskal(grafo):
    '''
    Dado un grafo (en formato de listas con pesos), aplica el algoritmo de 
    Kruskal y retorna el MST correspondiente (o un bosque, en el caso de que 
    no sea conexo).
    '''
    nodos, aristas = grafo
    queue = pqueue.pqueue()
    dset = unionfind.UnionFind()
    for nodo in nodos:
        dset[nodo]
    for arista in aristas:
        queue[arista[:2]] = arista[2]
    aristas_arbol = list()
    while queue.size > 0:
        arista, peso = queue.pop()
        a, b = arista
        if a != b and dset[a] != dset[b]:
            aristas_arbol.append((a,b,peso))
            dset.union(a,b)
    return [nodos[:], aristas_arbol]


def main():
    pass


if __name__ == "__main__":
    main()
