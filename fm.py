import tkinter as tk
import tkinter.filedialog
import fruchterman as fr


class Root(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.canv = tk.Canvas(self, width = 500, height = 500)
        self.canv.pack(side='top')
        tk.Button(self, text='Start', command = self.start).pack(side='bottom')
        tk.Button(self, text='Stop', command = self.stop).pack(side='bottom')
        tk.Button(self, text='Load', command = self.load).pack(side='bottom')
        self.task = 0
    
    def load(self):
        self.stop()
        file_name = tkinter.filedialog.askopenfilename()
        with open(file_name, mode = 'r') as f:
            vertex = list()
            for i in range(int(f.readline().rstrip())):
                vertex.append(f.readline().rstrip())
            edges = list()
            edge = f.readline()
            while edge != '':
                edges.append(edge.split())
                edge = f.readline()
        self.graph = [vertex, edges]
        x,y = 30*len(vertex), 20*len(vertex)
        self.canv.config(width = x, height = y)
        self.positions = fr.fruchterman(x-32,y-32,self.graph)
        self.draw()

    def start(self):
        self.draw()
        self.task = self.after(500, self.start)

    def stop(self):
        if self.task:
            self.after_cancel(self.task)

    def draw(self):
        self.canv.delete('all')
        pos = next(self.positions)
        for v in pos:
            self.canv.create_oval(pos[v].x - 8, pos[v].y + 8,
                                  pos[v].x + 8, pos[v].y - 8,
                                  fill = 'black')
        for e in self.graph[1]:
            self.canv.create_line(pos[e[0]].x, pos[e[0]].y,
                                  pos[e[1]].x, pos[e[1]].y)



if __name__ == '__main__':
    root = Root()
    root.mainloop()
