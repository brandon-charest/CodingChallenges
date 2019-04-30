class Node(object):
    def __init__(self, data="$", left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __bool__(self):
        return self.data != "$"

    def __str__(self):
        buf, out = [self], []
        while buf:
            out.append("{}".format([node.data for node in buf]))
            if any(node for node in buf):
                children = []
                for node in buf:
                    for subnode in (node.left, node.right):
                        children.append(subnode if subnode else Node())
                buf = children
            else:
                break
        return "\n".join(out)


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
        if node is None:
            return
        self._inorder(node.left)
        print(node.data)
        self._inorder(node.right)

    def _postorder(self, node):
        if node is None:
            return
        self._preorder(node.left)
        self._preorder(node.right)
        print(node.data)

    def _preorder(self, node):
        if node is None:
            return
        else:
            print(node.data, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

    def print_tree(self):
        print(self.root)


if __name__ == "__main__":
    tree = BinarySearchTree()
    elements = [27,14,35,10,19,31,42]

    for e in elements:
        tree.insert(e)

    tree.print_tree()
