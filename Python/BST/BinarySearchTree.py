class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node[Data={self.data}]"


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            node = Node(data)
        elif self.root.data > data:
            node.left = self._insert(node.left, data)
        elif self.root.data < data:
            node.right = self._insert(node.right, data)

        return node

    def traversal(self, order_type=None):

        if order_type == "in":
            self._inorder(self.root)
        elif order_type == "post":
            self._postorder(self.root)
        else:
            self._preorder(self.root)

    def _inorder(self, node):
        pass

    def _postorder(self, node):
        pass

    def _preorder(self, node):
        if node is None:
            return
        else:
            print(node.data)
            self._preorder(node.left)
            self._preorder(node.right)


tree = BinarySearchTree()
elements = [1,9,4,3,5,7,10,0]

for e in elements:
    tree.insert(e)
tree.traversal()
