from itertools import combinations
from math import sqrt
from random import random


class point:
    def __init__(self, posx = 0, posy = 0):
        self.x = posx
        self.y = posy
    def __add__(self,other):
        return point(self.x + other.x, self.y + other.y)
    def __mul__(self,scalar):
        return point(self.x * scalar, self.y * scalar)
    def __sub__(self,other):
        return point(self.x - other.x, self.y - other.y)
    def __truediv__(self,scalar):
        return point(self.x / scalar, self.y / scalar)


class Fruchterman():
    def __init__(self,X,Y,G):
        self.x, self.y = X, Y
        self.area = X*Y
        self.V, self.E = G
        self.k = 0.5*sqrt(self.area/len(G[0]))
        self.temp = X / 4
        self.random_start()

    def __iter__(self):
        return self

    def __next__(self):
        if self.temp > 10**-3:
            self.calc_rep_forces()
            self.calc_attract_forces()
            self.calc_position()
            self.temp *= 7/8
            return (self.position, self.temp)
        else:
            raise StopIteration

    def random_start(self):
        self.position = dict()
        for vertex in self.V:
           self.position[vertex] = point(random()*self.x,random()*self.y)

    def calc_rep_forces(self):
        self.accum = dict()
        for v in self.position:
            self.accum[v] = point()
        for a,b in combinations(self.position.keys(), 2):
            # Calculo para a
            delta = self.position[a] - self.position[b]
            delta_abs = delta.x**2 + delta.y**2
            self.accum[a] = self.accum[a] + delta * self.k**2 / delta_abs
            # Calculo para b
            delta = self.position[b] - self.position[a]
            self.accum[b] = self.accum[b] + delta * self.k**2 / delta_abs

    def calc_attract_forces(self):
        for edge in self.E:
            delta = self.position[edge[0]] - self.position[edge[1]]
            delta_abs = sqrt(delta.x**2 + delta.y**2)
            self.accum[edge[0]] = self.accum[edge[0]] - delta * delta_abs / self.k
            self.accum[edge[1]] = self.accum[edge[1]] + delta * delta_abs / self.k

    def calc_position(self):
        for v in self.position:
            disp_abs = sqrt(self.accum[v].x**2 + self.accum[v].y**2)
            disp_mag = min(disp_abs, self.temp)
            disp = self.accum[v] / disp_abs * disp_mag
            self.position[v] = self.position[v] + disp
            self.position[v].x = self.x if self.position[v].x > self.x else 0 if self.position[v].x < 0 else self.position[v].x
            self.position[v].y = self.y if self.position[v].y > self.y else 0 if self.position[v].y < 0 else self.position[v].y
