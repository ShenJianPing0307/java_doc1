class Node:

    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class Tree:

    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if not self.root:
            self.root = node
        else:
            queue = []
            queue.append(node)
            while queue:
                cur = queue.pop(0)
                if not cur.lchild:
                    cur.lchild = node
                    return
                elif not cur.rchild:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)