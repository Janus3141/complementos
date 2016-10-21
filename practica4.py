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
    aristas = grafo[1]
    aristas = aristas[:]
    queue = pqueue.pqueue()
    queue.add(vertice, 0)
    result = dict()
    while queue.size > 0:
        nodo, dist = queue.pop()
        result[nodo] = dist
        aristas2 = list() # Aristas no procesadas
        while len(aristas) != 0:
            a = aristas.pop()
            if a[0] == a[1]:
                continue
            elif nodo == a[0]:
                nodo_dest = a[1]
            elif nodo == a[1]:
                nodo_dest = a[0]
            else:
                aristas2.append(a)
                continue
            dist_dest = dist+a[2]
            if nodo_dest not in queue:
                queue.add(nodo_dest, dist_dest)
            elif queue[nodo_dest] > dist_dest:
                queue[nodo_dest] = dist_dest
        aristas = aristas2
    return result


def dijkstra_2(grafo, vertice):
    '''
    Dado un grafo (en formato de listas con pesos), aplica el algoritmo de 
    Dijkstra para hallar el CAMINO mas corto desde el vertice de origen
    a cada uno del resto de los vertices.
    Formato resultado: {'a': ['a'], 'b': ['a', 'b'], 'c': ['a', 'c']}
    (Nodos que no son claves significa que no hay camino a ellos)
    '''
    aristas = grafo[1]
    aristas = aristas[:]
    queue = pqueue.pqueue()
    queue.add(vertice, 0)
    result = {vertice:[vertice]}
    while queue.size > 0:
        nodo, dist = queue.pop()
        aristas2 = list() # Aristas no procesadas
        while len(aristas) != 0:
            a = aristas.pop()
            if a[0] == a[1]:
                continue
            elif nodo == a[0]:
                nodo_dest = a[1]
            elif nodo == a[1]:
                nodo_dest = a[0]
            else:
                aristas2.append(a)
                continue
            dist_dest = dist+a[2]
            if nodo_dest not in queue:
                queue.add(nodo_dest, dist_dest)
                result[nodo_dest] = result[nodo]+[nodo_dest]
            elif queue[nodo_dest] > dist_dest:
                queue[nodo_dest] = dist_dest
                result[nodo_dest] = result[nodo]+[nodo_dest]
        aristas = aristas2
    return result


def main():
    pass

if __name__ == "__main__":
    main()
