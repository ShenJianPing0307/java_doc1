"""
先进先去
"""


class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == None

    def push(self, item):
        self.items.append(item)

    def pull(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[self.size() - 1]

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pull())

