class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Link:

    def __init__(self):
        self._head = None

    def add(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node

    def travel(self):
        cur = self._head

        while cur:
            print(cur.data)
            cur = cur.next
        print("")

    def length(self):

        cur = self._head

        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def is_empty(self):

        return self._head == None

    def append(self, item):
        node = Node(item)
        cur = self._head
        if self.is_empty():
            self._head = node
        while cur:
            cur = cur.next

        cur.next = node

    def insert(self, pos, item):

        node = Node(item)
        if pos <= 0:
            self.add(item)

        elif pos > self.length() - 1:
            self.append(item)

        else:
            count = 0
            pre = self._head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def search(self, item):

        cur = self._head

        while cur:
            if cur.data == item:
                return True
            cur = cur.next
        return False

    def remove(self, item):

        pre = None
        cur = self._head

        while cur:

            if cur.data == item:

                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = pre










if __name__ == '__main__':
    link = Link()
    link.add(2)
    link.add(3)
    link.add(4)
    link.travel()
    link.insert(2, 5)
    link.travel()
    print(link.is_empty())
