import tkinter as tk
import tkinter.filedialog
import fruchterman as fr


class Root(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.t = tk.StringVar()
        self.canv = tk.Canvas(self, width = 800, height = 500)
        self.canv.pack(side='top')
        self.startb = tk.Button(self, text='Start', command = self.start, state='disabled')
        self.startb.pack(side='left')
        self.stepb = tk.Button(self, text='Step', command = self.step, state='disabled')
        self.stepb.pack(side='left')
        tk.Button(self, text='Stop', command = self.stop).pack(side='left')
        tk.Button(self, text='Load', command = self.load).pack(side='left')
        tk.Label(self, textvariable=self.t,bg='red',fg='white').pack(side='right')
        self.task = 0
    
    def load(self):
        self.stop()
        file_name = tkinter.filedialog.askopenfilename()
        if file_name == '':
            return
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
        # x,y = 60*len(vertex), 40*len(vertex)
        # self.canv.config(width = x, height = y)
        self.positions = fr.fruchterman(800-32,500-32,self.graph)
        self.draw()
        self.startb.config(state='normal')
        self.stepb.config(state='normal')

    def start(self):
        self.draw()
        self.task = self.after(50, self.start)

    def stop(self):
        if self.task:
            self.after_cancel(self.task)

    def step(self):
        if self.task:
            self.after_cancel(self.task)
        self.draw()

    def draw(self):
        try:
            pos,temp = next(self.positions)
        except StopIteration:
            self.startb.config(state='disabled')
            self.stepb.config(state='disabled')
            return
        self.canv.delete('all')
        self.t.set('Temp: ' + str(temp))
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
