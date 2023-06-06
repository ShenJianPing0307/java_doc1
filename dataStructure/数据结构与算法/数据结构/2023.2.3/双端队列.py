# from collections import deque


# queue = deque()
#
# queue.append(1)
# queue.append(2)
# queue.appendleft(3)
# print(queue)
# print(queue.pop())
# print(queue)


class Deque:

    def __init__(self):
        self.leftStack = []
        self.BufferStack = []
        self.rightStack = []

    def is_empty(self):
        return not self.leftStack and not self.rightStack

    def PUT(self, x):
        """将x 附加到序列的开头"""
        self.leftStack.append(x)

    def PUSH(self, x):
        """将 x 附加到序列的末尾。"""
        self.rightStack.append(x)

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
            mid = len(self.rightStack) // 2
            # left:[]   buffer: [4] right:[3]
            for i in range(mid):
                self.BufferStack.append(self.rightStack.pop())

            # left:[3] buffer: [4] right:[]
            while self.rightStack:
                self.leftStack.append(self.rightStack.pop())

            # left:[3] buffer: [] right:[4]
            while self.BufferStack:
                self.rightStack.append(self.BufferStack.pop())

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
            mid = len(self.leftStack) // 2

            # left:[2]   buffer: [1] right:[]
            for i in range(mid):
                self.BufferStack.append(self.leftStack.pop())

            # left:[] buffer: [1] right:[2]
            while self.leftStack:
                self.rightStack.append(self.leftStack.pop())

            # left:[1] buffer: [] right:[2]
            while self.BufferStack:
                self.leftStack.append(self.BufferStack.pop())

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
"""
1
4
3
2
"""
