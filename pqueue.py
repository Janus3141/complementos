class pqueue():
    def __init__(self):
        self.queue = list()
        self.queue.append('dummy')
        self.size = 0

    def __contains__(self, x):
        for i in range(1, self.size+1):
            if (self.queue[i])[0] == x:
                return True
        return False

    def __getitem__(self, x):
        for i in range(1, self.size+1):
            if (self.queue[i])[0] == x:
                return (self.queue[i])[1]
        raise KeyError

    def __setitem__(self, x, y):
        for i in range(1, self.size+1):
            if (self.queue[i])[0] == x:
                (self.queue[i])[1] == y
                return
        raise KeyError

    def add(self, item, priority):
        self.queue.append([item,priority])
        self.size += 1
        i = self.size//2
        j = self.size
        while i != 0:
            if (self.queue[i])[1] > priority:
                self.queue[j] = self.queue[i]
                self.queue[i] = [item,priority]
                j = i
                i = j//2
            else:
                break

    def pop(self):
        if self.size == 0:
            raise IndexError("Empty queue.")
        a = self.queue[1]
        self.queue[1] = self.queue[self.size]
        del self.queue[self.size]
        self.size -= 1
        i = 1
        while i <= self.size//2:
            if i*2 < self.size:
                minimum = i*2 if (self.queue[i*2])[1] <= (self.queue[i*2+1])[1] else i*2+1
            else:
                minimum = i*2
            if (self.queue[i])[1] > (self.queue[minimum])[1]:
                temp = self.queue[i]
                self.queue[i] = self.queue[minimum]
                self.queue[minimum] = temp
            else:
                break
        return a
