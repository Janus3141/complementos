#! /usr/bin/python

# 1ra Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

import sys
import pprint

grafo_adyacencia1 = (
    ["A", "B", "C", "D"], 
    [[0, 1, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0],]
)

grafo_adyacencia2 = (
    ["A", "B", "C", "D"], 
    [[0, 2, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0],]
)

def leer_grafo_stdin():
    nvertices = input()
    vertices = []
    aristas = []
    try:
        for i in range(nvertices):
            line = raw_input()
            vertices.append(line.rstrip())
        while True:
            line = raw_input()
            aristas.append(line.split())
    except EOFError:
	return (vertices, aristas)


def imprime_grafo_lista(grafo):
	pprint.pprint(grafo)


def lista_a_incidencia(grafo_lista):
	matriz_incidencia = [[2 if vertice == arista[0] and  vertice == arista[1]
					else -1 if vertice == arista[0]
					else 1 if vertice == arista[1]
					else 0
					for vertice in grafo_lista[0]
					]
				for arista in grafo_lista[1]
				]
	return (grafo_lista[0], transp(matriz_incidencia)


def transp(matrix):
	if not matrix:
		return matrix
	return zip(*matrix)

def incidencia_a_lista(grafo_incidencia):
	matriz_incidencia = transp(grafo_incidencia[1])
	grafo_lista = []
	for arista in matriz_incidencia:
		for vertice, i in zip(grafo_incidencia[0], arista):
			if i == -1:
				a = vertice
			elif i == 1:
				b = vertice
			elif i == 2:
				a = vertice
				b = vertice
		grafo_lista.append([a,b])
	return (grafo_incidencia[0], grafo_lista)


def imprime_grafo_incidencia(grafo_incidencia):
    '''
    Muestra por pantalla un grafo. 
    El argumento esta en formato de matriz de incidencia.
    '''
    pass


def lista_a_adyacencia(grafo_lista):
	return (grafo_lista[0],
		[[1 if [x,y] in grafo_lista[1] else 0
				for y in grafo_lista[0]]
				for x in grafo_lista[0]]
		)


def adyacencia_a_lista(grafo_adyacencia):
	pass


def imprime_grafo_adyacencia(grafo_adyacencia):
    '''
    Muestra por pantalla un grafo. 
    El argumento esta en formato de matriz de adyacencia.
    '''
    pass


def leer_grafo_archivo(file_path):
    '''
    Lee un grafo desde un archivo y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    '''
    pass



if __name__ == "__main__":
	graf = leer_grafo_stdin()
	imprime_grafo_lista(graf)
	graf = lista_a_incidencia(graf)
	print(graf)
	graf = incidencia_a_lista(graf)
	print(graf)
