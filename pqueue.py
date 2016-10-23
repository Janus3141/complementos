class PQueue():
    def __init__(self):
        self._order = list()

    def size(self):
        return len(self._order)

    def get(self,i):
        return self._order[i-1]

    def insert(self,i,j):
        if i > 1:
            self._order[i-1] = j
        else:
            self._order.append(j)

    def __contains__(self, x):
        for i in range(1, self.size()):
            if (self.get(i))[0] == x:
                return True
        return False

    def __getitem__(self, x):
        for i in range(1, self.size()):
            if (self.get(i))[0] == x:
                return (self.get(i))[1]
        raise KeyError

    def __setitem__(self, item, priority):
        self._order.append([item,priority])
        i = self.size()//2
        j = self.size()
        while i != 0:
            if (self.get(i))[1] > priority:
                self.insert(j, self.get(i))
                self.insert(i, [item,priority])
                j = i
                i = j//2
            else:
                break

    '''    def set_prior(self,item,priority):       Arreglar, implementar reordenamiento de array
            for i in range(1, self.size()):
                if (self.get(i))[0] == item:
                    self.insert(i, [item,priority])
                    return
            raise KeyError
    '''
    def deq(self):
        if self.size() == 0:
            raise IndexError("Empty queue")
        a = self.get(1)
        self.insert(1, self._order.pop(self.size()))
        i = 1
        while i <= self.size()//2:
            if i*2+1 <= self.size():
                minimum = i*2 if (self.get(i*2))[1] <= (self.get(i*2+1))[1] else i*2+1
            else:
                minimum = i*2
            if (self.get(i))[1] > (self.get(minimum))[1]:
                temp = self.get(i)
                self.insert(i, self.get(minimum))
                self.insert(minimum, temp)
                i = minimum
            else:
                break
        return a
