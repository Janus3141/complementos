import pqueue

def main():
    q = pqueue.PQueue()
    for a,b in zip('abcdefghij', [14,66,1,42,6,44,8764,4124,51,22]):
        q[a] = b
    for i in range(10):
        print(q._order)
        print(q.deq())
        print(' ')

if __name__ == '__main__':
    main()
