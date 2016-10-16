class pqueue():
    def __init__(self):
        self.queue = list()
        self.queue.append('dummy')
        self.size = 0

    def add(self, item, priority):
        self.queue.append([item,priority])
        size += 1
        i = self.size//2
        j = size
        while i != 0:
            if (self.queue[i])[1] > priority:
                (self.queue[j])[0] = (self.queue[i])[0]
                (self.queue[i])[0] = item
                j = i
                i = j//2
            else:
                break

    def pop(self):
        if size == 0:
            raise IndexError("Empty queue.")
        a = self.queue[1]
        self.queue[1] = self.queue.pop[size]
        size -= 1
        i = 1
        while i <= self.size//2:
            if i*2 < size:
                minimum = i*2 if self.queue[i*2] <= self.queue[i*2+1] else i*2+1
            else:
                minimum = i*2
            if self.queue[i] > self.queue[minimum]:
                temp = self.queue[i]
                self.queue[i] = self.queue[minimum]
                self.queue[minimum] = temp
            else:
                break
        return a
