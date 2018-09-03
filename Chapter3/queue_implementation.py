class Queue:
    def __init__(self):
        self.items = []

    def enque(self,item):
        self.items.insert(0,item)

    def deque(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def isempty(self):
        return self.items == []

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    print(q.isempty())
    print(q.size())
    q.enque(1)
    q.enque(2)
    q.enque(3)
    q.enque(4)
    print(q.isempty())
    print(q.size())
    print(q.peek())
    print(q.deque())
