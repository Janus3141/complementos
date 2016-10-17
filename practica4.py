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
    result = dict()
    while queue.size > 0:
        nodo, dist = queue.pop()
        result[nodo] = dist
        for i, arista in aristas:
            if nodo == arista[0]:
                nodo_dest = arista[1]
            elif nodo == arista[1]:
                nodo_dest = arista[0]
            else:
                continue
            dist_dest = dist+arista[2]
            if nodo_dest not in queue:
                queue.add(nodo_dest, dist_dest)
            elif queue[nodo_dest] > dist_dest:
                queue[nodo_dest] = dist_dest
            del aristas[i]
    return result


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
