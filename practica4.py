#! /usr/bin/python

# 4ta Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

import pqueue

def dijkstra(grafo, vertice):
    '''
    Dado un grafo (en formato de listas con pesos), aplica el algoritmo de 
    Dijkstra para hallar el COSTO del camino mas corto desde el vertice de origen
    al resto de los vertices.
    Formato resultado: {'a': 10, 'b': 5, 'c': 0}
    (Nodos que no son claves significa que no hay camino a ellos)
    '''
    nodos, aristas = grafo
    queue = pqueue.pqueue()
    nodos.remove(vertice)
    queue.add(vertice, 0)
    while queue.size > 0:
        nodo = queue.pop()
        for i, arista in aristas:
            if nodo in arista:
                
    return {}


def dijkstra_2(grafo, vertice):
    '''
    Dado un grafo (en formato de listas con pesos), aplica el algoritmo de 
    Dijkstra para hallar el CAMINO mas corto desde el vertice de origen
    a cada uno del resto de los vertices.
    Formato resultado: {'a': ['a'], 'b': ['a', 'b'], 'c': ['a', 'c']}
    (Nodos que no son claves significa que no hay camino a ellos)
    '''
    return {}


def main():
    pass

if __name__ == "__main__":
    main()
