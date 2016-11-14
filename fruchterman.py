from itertools import combinations
from math import sqrt
from random import random


class point:
    def __init__(self, posx = 0, posy = 0):
        self.x = posx
        self.y = posy
    def __sum__(self,other):
        return point(self.x + other.x, self.y + other.y)
    def __mul__(self,scalar):
        return point(self.x * scalar, self.y * scalar)
    def __sub__(self,other):
        return point(self.x - other.x, self.y - other.y)
    def __truediv__(self,scalar):
        return point(self.x / scalar, self.y / scalar)


def fruchterman(X, Y, G):
    area = X*Y
    k = sqrt(area/len(G[0]))
    V, E = G
    position = random_start(X, Y, V)
    temp = X / 20
    for i in range(algunrange):
        accum = calc_rep_forces(position,k)
        accum = calc_attract_forces(position,E,k,accum)
        position = calc_position(position, accum, temp, X, Y)
        temp = cool(temp)
        draw(position)


def random_start(x, y, v):
    position = dict()
    for vertex in v:
       position[vertex] = point(random()*x,random()*y)
    return position


def calc_rep_forces(position,k):
    accum = dict()
    for v in position:
        accum[v] = point()
    for a,b in combinations(position.keys()):
        # Calculo para a
        delta = position[a] - position[b]
        delta_abs = delta.x**2 + delta.y**2
        accum[a] = accum[a] + delta * k**2 / delta_abs
        # Calculo para b
        delta = position[b] - position[a]
        accum[b] = accum[b] + delta * k**2 / delta_abs
    return accum


def calc_attract_forces(position, E, k, accum):
    for edge in E:
        delta = position[edge[0]] - position[edge[1]]
        delta_abs = sqrt(delta.x**2 + delta.y**2)
        accum[edge[0]] = accum[edge[0]] - delta * delta_abs / k
        accum[edge[1]] = accum[edge[1]] + delta * delta_abs / k
    return accum


def calc_position(position, accum, temp, w, l):
    for v in position:
        disp_abs = sqrt(accum[v].x**2 + accum[v].y**2)
        disp_mag = min(disp_abs, temp)
        disp = accum[v] / disp_abs * disp_mag
        position[v] = position[v] + disp
        position[v].x = w if position[v].x > w else 0 if position[v].x < 0 else position[v].x
        position[v].y = l if position[v].y > l else 0 if position[v].y < 0 else position[v].y
    return position


def cool(t):
    return t*3/4


def draw(pos):
    pass
