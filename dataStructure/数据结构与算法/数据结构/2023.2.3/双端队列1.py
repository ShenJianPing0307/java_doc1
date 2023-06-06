
class Stack:

    def __init__(self):
        """使用顺序表结构存储数据"""
        self._list = []

    def is_empty(self):
        """判断栈是否是空的"""
        return self._list == []

    def push(self, item):
        """添加元素,从尾部加元素，再从尾部取元素，复杂度为O(1)"""
        self._list.append(item)

    def pop(self):
        """取出元素"""
        return self._list.pop()

    def peek(self):
        """返回栈顶元素"""
        return self._list[len(self._list) - 1]

    def size(self):
        """返回栈的大小"""
        return len(self._list)

class Deque:

    def __init__(self):
        self.leftStack = Stack()
        self.BufferStack = Stack()
        self.rightStack = Stack()

    def is_empty(self):
        return not self.leftStack and not self.rightStack

    def PUT(self, x):
        """将x 附加到序列的开头"""
        self.leftStack.push(x)

    def PUSH(self, x):
        """将 x 附加到序列的末尾。"""
        self.rightStack.push(x)

    """
         ->       <-
          1 2 | 3 4
         <-       ->
    """

    # | 3 4
    def PULL(self):
        """返回序列中的第一个元素"""
        if self.leftStack:
            return self.leftStack.pop()
        if self.is_empty():
            return None
        else:
            mid = self.rightStack.size() // 2
            # left:[]   buffer: [4] right:[3]
            for i in range(mid):
                self.BufferStack.push(self.rightStack.pop())

            # left:[3] buffer: [4] right:[]
            while self.rightStack:
                self.leftStack.push(self.rightStack.pop())

            # left:[3] buffer: [] right:[4]
            while self.BufferStack:
                self.rightStack.push(self.BufferStack.pop())

            return self.leftStack.pop()

    # // 1 2 |
    def POP(self):
        """返回序列中的最后一个元素"""
        if self.rightStack:
            return self.rightStack.pop()
        if self.is_empty():
            return None
        else:
            # left:[1,2] buffer:[] right:[]
            mid = self.leftStack.size() // 2

            # left:[2]   buffer: [1] right:[]
            for i in range(mid):
                self.BufferStack.push(self.leftStack.pop())

            # left:[] buffer: [1] right:[2]
            while self.leftStack:
                self.rightStack.push(self.leftStack.pop())

            # left:[1] buffer: [] right:[2]
            while self.BufferStack:
                self.leftStack.push(self.BufferStack.pop())

            return self.rightStack.pop()


deque = Deque()

deque.PUT(2)
deque.PUSH(3)
deque.PUSH(4)
deque.PUT(1)
print(deque.PULL())
print(deque.POP())
print(deque.POP())
print(deque.PULL())