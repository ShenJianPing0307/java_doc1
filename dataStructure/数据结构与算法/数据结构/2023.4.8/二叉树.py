
class Node:

    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree:

    def __init__(self):
        self.root = None

    def add(self, data):
        node = Node(data)

        if not self.root:
            self.root = node
        else:
            queue = [node]

            while queue:

                cur = queue.pop(0)

                if not cur.lchild:
                    queue.append(cur.lchild)
                    return
                elif not cur.rchild:
                    queue.append(cur.rchild)
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)


