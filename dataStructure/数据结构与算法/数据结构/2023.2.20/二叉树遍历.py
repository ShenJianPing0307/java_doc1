
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

    def breath_travel(self, root):

        if not root:
            return
        queue = []
        queue.append(root)

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

    def post_order(self, root):
        if not root:
            return
        self.post_order(root.lchild)
        self.post_order(root.rchild)
        print(root.data)
        

if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    print(tree.root.lchild)
    # tree.breath_travel(tree.root)
