from random import random
import tkinter as tk
from time import sleep


class point():
    def __init__(self,x,y):
        self.x = x
        self.y = y



def main():
    V = [1,2,3,4,5,6,7,8]
    E = [[1,2],[2,3],[4,5],[1,7],[6,3]]
    root = tk.Tk()
    canv = tk.Canvas(root,width=500,height=500)
    canv.pack()
    position = dict()
    for v in V:
        position[v] = point(random()*500, random()*500)
        canv.create_oval(position[v].x-8, position[v].y+8,
                         position[v].x+8, position[v].y-8,
                         fill = 'black')
    for e in E:
        canv.create_line(position[e[0]].x, position[e[0]].y,
                         position[e[1]].x, position[e[1]].y)
    tk.Button(root, text='delete',command = lambda: canv.delete('all')).pack()
    root.mainloop()


if __name__ == '__main__':
    main()
