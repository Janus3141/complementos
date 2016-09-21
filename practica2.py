#! /usr/bin/python

# 2da Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

# Un disjointSet lo representaremos como un diccionario. 
# Ejemplo: {"A":1, "B":2, "C":1} (Nodos A y C pertenecen al conjunto 
# identificado con 1, B al identificado on 2)

def make_set(lista):
    '''
    Inicializa un conjunto (Lista) de modo de que todos sus elementos pasen 
    a ser conjuntos unitarios. 
    Retorna un disjointSet
    '''
    return dict(zip(lista,range(len(lista))))


def find(elem, disjoint_set):
    '''
    Obtiene el identificador correspondiente al conjunto al que pertenece 
    el elemento 'elem'
    '''
    return disjoint_set[elem]


def union(id_1, id_2, disjoint_set):
    '''
    Une los conjuntos con identificadores id_1, id_2.
    Retorna la estructura actualizada
    '''
    return {x:(disjoint_set[x] if disjoint_set[x] != id_2 else id_1) for x in disjoint_set}


def componentes_conexas(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas.
    Ejemplo formato salida: 
        [['a, 'b'], ['c'], ['d']]
    '''
    nodos, aristas = grafo_lista
    ds = make_set(nodos)
    for nodo1, nodo2 in aristas:
	id1 = find(nodo1, ds)
        id2 = find(nodo2, ds)
        if id1 != id2:
            ds = union(id1, id2, ds)



def main():
    pass

if __name__ == "__main__":
    main()
