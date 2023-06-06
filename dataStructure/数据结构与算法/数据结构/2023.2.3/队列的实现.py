"""
队列的实现
"""


class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Queue:

    def __init__(self):
        self.Sin = []
        self.Sout = []

    def put(self, value):
        self.Sin.append(value)

    def pull(self):
        if self.Sout:  # Sout栈非空
            return self.Sout.pop()
        if not self.Sin:  # Sin栈非空
            return -1
        while self.Sin:
            self.Sout.append(self.Sin.pop())
        return self.Sout.pop()
