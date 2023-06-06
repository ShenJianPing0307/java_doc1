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

    def breath_travel(self):

        if not self.root:
            return

        queue = [self.root]

        while queue:

            cur = queue.pop(0)
            print(cur.data)

            if cur.lchild:
                queue.append(cur.lchild)
            if cur.rchild:
                queue.append(cur.rchild)

    def pre_order(self, root):

        if not root:
            return
        print(root.data)
        self.pre_order(root.lchild)
        self.pre_order(root.rchild)

    def middle_order(self, root):
        if not root:
            return
        self.middle_order(root.lchild)
        print(root.data)
        self.middle_order(root.rchild)

    def after_order(self, root):
        if not root:
            return
        self.after_order(root.lchild)
        self.after_order(root.rchild)
        print(root.data)
