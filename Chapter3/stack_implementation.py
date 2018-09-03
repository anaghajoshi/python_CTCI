class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) -1]

    def isempty(self):
        return self.items == []

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s.isempty())
    print(s.size())
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.isempty())
    print(s.size())
    print(s.peek())
    print(s.pop())
