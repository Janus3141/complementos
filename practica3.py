#! /usr/bin/python

# 3ra Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos


# Referencias:
# pygraphMl    : http://hadim.github.io/pygraphml/usage.html
# GraphML      : http://graphml.graphdrawing.org/
# XML          : http://www.w3schools.com/xml/
# Editores     : http://www.cs.bilkent.edu.tr/~ivis/layout/demo/lw1x.html
#                http://cytoscapeweb.cytoscape.org/demo
#                http://cytoscape.org/
# elementTree  : http://docs.python.org/2/library/xml.etree.elementtree.html 


def leer_grafo_peso_stdin():
    '''
    Lee un grafo desde entrada estandar y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B 2.1
        B C -3
        C B
    Ejemplo retorno: 
        (['A','B','C'],[('A','B', 2.1),('B','C', -3),('C','B', None)])
    '''
    nvertices = input()
    vertices = list()
    aristas = list()
    for i in range(nvertices):
        vertices.append(raw_input())
    try:
        while True:
            arista = raw_input().split()
            try:
                 arista[2] = float(arista[2])
            except IndexError:
                 arista.append(None)
            aristas.append(arista)
    except EOFError:
        return (vertices, aristas)


def imprime_grafo_peso_lista(grafo):
    '''
    Muestra por pantalla un grafo. El argumento esta en formato de lista.
    '''
    for v in grafo[0]:
        print v
    for v1, v2, w in grafo[1]:
        print v1, v2, w


def leer_grafo_peso_archivo(file_path):
    '''
    Lee un grafo desde un archivo y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B 2.1
        B C -3
        C B
    Ejemplo retorno: 
        (['A','B','C'],[('A','B', 2.1),('B','C', -3),('C','B', None)])
    '''
    with open(file_path, mode = 'r') as f:
        nvertices = int(f.readline().rstrip())
        vertices = list()
        aristas = list()
        for i in range(nvertices):
            vertices.append(f.readline().rstrip())
        arista = f.readline()
        while arista != '':
            arista = arista.split()
            try:
                arista[2] = float(arista[2])
            except IndexError:
                arista.append(None)
            aristas.append(arista)
            arista = f.readline()
        else:
            return (vertices, aristas)


def lee_graphml(file_path):
    '''
    Lee un grafo en formato graphML usando la libreria pygraphMl, 
    y lo devuelve como lista con pesos
    '''
    pass


def lee_graphml_2(file_path):
    '''
    OPCIONAL
    Lee un grafo en formato graphML, recorriendo el XML con la libreria 
    elementTree (xml.etree.ElementTree), y lo devuelve como lista con pesos
    '''
    pass





def main():
    g = leer_grafo_peso_archivo('g.txt')
    imprime_grafo_peso_lista(g)

if __name__ == '__main__':
    main()
